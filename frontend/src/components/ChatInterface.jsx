import React, { useState, useRef, useEffect } from 'react'
import { farmAPI } from '../services/api'

const ChatInterface = () => {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: 'Olá! Sou o assistente AgriSmart Brasil. Posso ajudar você com análises de clima, culturas, irrigação, previsão de produção e gestão da fazenda. Como posso ajudar hoje?',
      agent: 'farm_manager',
    },
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const sendMessage = async () => {
    if (!input.trim()) return

    const userMessage = input.trim()
    setInput('')
    setMessages((prev) => [...prev, { role: 'user', content: userMessage }])
    setLoading(true)

    try {
      const data = await farmAPI.chat(userMessage, {
        location: 'São Paulo, Brasil',
        crops: ['Soja', 'Milho', 'Café'],
        season: 'Verão 2025',
      })

      // Formatar a resposta se vier como JSON
      let formattedContent = data.response || 'Desculpe, ocorreu um erro ao processar sua solicitação.'
      
      // Tentar parsear se for JSON string
      try {
        if (typeof formattedContent === 'string' && (formattedContent.trim().startsWith('{') || formattedContent.trim().startsWith('['))) {
          const parsed = JSON.parse(formattedContent)
          formattedContent = JSON.stringify(parsed, null, 2)
        }
      } catch (e) {
        // Se não for JSON válido, manter o texto original
      }

      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: formattedContent,
          agent: data.agent || 'farm_manager',
        },
      ])
    } catch (error) {
      console.error('Error:', error)
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: 'Desculpe, não foi possível conectar ao servidor. Verifique se a API está rodando.',
          agent: 'error',
        },
      ])
    } finally {
      setLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  const quickQuestions = [
    'Qual a melhor época para plantar milho?',
    'Como está o clima para os próximos dias?',
    'Preciso irrigar hoje?',
    'Qual a previsão de produção da safra?',
  ]

  const agentColors = {
    farm_manager: 'from-purple-500 to-pink-500',
    climate_monitor: 'from-blue-500 to-cyan-500',
    crop_analyzer: 'from-green-500 to-emerald-500',
    water_optimizer: 'from-cyan-500 to-blue-500',
    yield_predictor: 'from-yellow-500 to-orange-500',
    error: 'from-red-500 to-rose-500',
  }

  return (
    <div className="h-[calc(100vh-280px)] flex flex-col">
      {/* Chat Messages */}
      <div className="flex-1 bg-slate-800/50 backdrop-blur-lg rounded-t-xl border border-slate-700 border-b-0 overflow-y-auto p-6 space-y-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`flex items-start space-x-3 max-w-3xl ${
                message.role === 'user' ? 'flex-row-reverse space-x-reverse' : ''
              }`}
            >
              <div
                className={`w-10 h-10 rounded-full bg-gradient-to-br ${
                  message.role === 'user'
                    ? 'from-purple-400 to-pink-500'
                    : agentColors[message.agent] || agentColors.farm_manager
                } flex items-center justify-center text-white font-bold flex-shrink-0`}
              >
                {message.role === 'user' ? 'U' : 'AI'}
              </div>
              <div
                className={`rounded-2xl p-4 ${
                  message.role === 'user'
                    ? 'bg-gradient-to-br from-purple-500/20 to-pink-500/20 border border-purple-500/30'
                    : 'bg-slate-900/50 border border-slate-700'
                }`}
              >
                {message.role === 'assistant' && (
                  <div className="text-xs text-slate-400 mb-2 font-medium">
                    {message.agent === 'farm_manager' && '🌾 Gestor da Fazenda'}
                    {message.agent === 'climate_monitor' && '🌤️ Monitor Climático'}
                    {message.agent === 'crop_analyzer' && '🌱 Analisador de Culturas'}
                    {message.agent === 'water_optimizer' && '💧 Otimizador de Água'}
                    {message.agent === 'yield_predictor' && '📊 Preditor de Produção'}
                  </div>
                )}
                <p className="text-white whitespace-pre-wrap">{message.content}</p>
              </div>
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex justify-start">
            <div className="flex items-start space-x-3 max-w-3xl">
              <div className="w-10 h-10 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
                <svg className="animate-spin h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
              </div>
              <div className="bg-slate-900/50 border border-slate-700 rounded-2xl p-4">
                <p className="text-slate-400">Processando...</p>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Quick Questions */}
      {messages.length === 1 && (
        <div className="bg-slate-800/50 backdrop-blur-lg border-x border-slate-700 p-4">
          <p className="text-sm text-slate-400 mb-3">Perguntas rápidas:</p>
          <div className="grid grid-cols-2 gap-2">
            {quickQuestions.map((question, index) => (
              <button
                key={index}
                onClick={() => setInput(question)}
                className="text-left text-sm bg-slate-900/50 hover:bg-slate-700/50 border border-slate-700 hover:border-green-500/50 rounded-lg p-3 text-slate-300 hover:text-white transition-all"
              >
                {question}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Input Area */}
      <div className="bg-slate-800/50 backdrop-blur-lg rounded-b-xl border border-slate-700 p-4">
        <div className="flex items-end space-x-3">
          <div className="flex-1">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Digite sua pergunta sobre a fazenda..."
              rows="3"
              className="w-full bg-slate-900/50 border border-slate-700 rounded-lg p-3 text-white placeholder-slate-500 focus:outline-none focus:border-green-500/50 resize-none"
            />
          </div>
          <button
            onClick={sendMessage}
            disabled={loading || !input.trim()}
            className="px-6 py-3 bg-gradient-to-r from-green-500 to-blue-500 text-white rounded-lg font-medium hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed h-fit"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
            </svg>
          </button>
        </div>
        <p className="text-xs text-slate-500 mt-2">
          Pressione Enter para enviar, Shift+Enter para nova linha
        </p>
      </div>
    </div>
  )
}

export default ChatInterface

