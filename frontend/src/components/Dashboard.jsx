import React, { useState, useEffect } from 'react'
import { farmAPI } from '../services/api'

const Dashboard = ({ farmData }) => {
  const [loading, setLoading] = useState(false)
  const [briefing, setBriefing] = useState(null)

  const getDailyBriefing = async () => {
    setLoading(true)
    try {
      const data = await farmAPI.getDailyBriefing({
        ...farmData,
        date: new Date().toISOString().split('T')[0],
        season: 'Verão 2025',
        pending_tasks: 'Irrigação, Monitoramento de pragas',
        alerts: 'Temperatura elevada',
      })
      setBriefing(data)
    } catch (error) {
      console.error('Error fetching briefing:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-6">
      {/* Weather and Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-gradient-to-br from-blue-500/20 to-blue-600/20 backdrop-blur-lg rounded-xl p-6 border border-blue-500/30">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-blue-300 text-sm font-medium">Temperatura</p>
              <p className="text-3xl font-bold text-white mt-1">{farmData.temperature}°C</p>
            </div>
            <div className="w-12 h-12 bg-blue-500/30 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div className="bg-gradient-to-br from-cyan-500/20 to-cyan-600/20 backdrop-blur-lg rounded-xl p-6 border border-cyan-500/30">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-cyan-300 text-sm font-medium">Umidade</p>
              <p className="text-3xl font-bold text-white mt-1">{farmData.humidity}%</p>
            </div>
            <div className="w-12 h-12 bg-cyan-500/30 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-cyan-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
              </svg>
            </div>
          </div>
        </div>

        <div className="bg-gradient-to-br from-green-500/20 to-green-600/20 backdrop-blur-lg rounded-xl p-6 border border-green-500/30">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-green-300 text-sm font-medium">Área Total</p>
              <p className="text-3xl font-bold text-white mt-1">{farmData.totalArea} ha</p>
            </div>
            <div className="w-12 h-12 bg-green-500/30 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-green-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div className="bg-gradient-to-br from-purple-500/20 to-purple-600/20 backdrop-blur-lg rounded-xl p-6 border border-purple-500/30">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-purple-300 text-sm font-medium">Culturas Ativas</p>
              <p className="text-3xl font-bold text-white mt-1">{farmData.activeCrops.length}</p>
            </div>
            <div className="w-12 h-12 bg-purple-500/30 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-purple-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      {/* Daily Briefing */}
      <div className="bg-slate-800/50 backdrop-blur-lg rounded-xl p-6 border border-slate-700">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold text-white">Briefing Diário</h2>
          <button
            onClick={getDailyBriefing}
            disabled={loading}
            className="px-4 py-2 bg-gradient-to-r from-green-500 to-blue-500 text-white rounded-lg font-medium hover:shadow-lg transition-all disabled:opacity-50"
          >
            {loading ? (
              <span className="flex items-center space-x-2">
                <svg className="animate-spin h-4 w-4" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span>Gerando...</span>
              </span>
            ) : (
              'Gerar Briefing'
            )}
          </button>
        </div>

        {briefing ? (
          <div className="prose prose-invert max-w-none">
            <div className="bg-slate-900/50 rounded-lg p-4">
              <pre className="text-sm text-slate-300 whitespace-pre-wrap">{briefing.briefing}</pre>
            </div>
          </div>
        ) : (
          <div className="text-center py-12 text-slate-400">
            <svg className="w-16 h-16 mx-auto mb-4 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <p>Clique em "Gerar Briefing" para obter insights diários da sua fazenda</p>
          </div>
        )}
      </div>

      {/* Active Crops */}
      <div className="bg-slate-800/50 backdrop-blur-lg rounded-xl p-6 border border-slate-700">
        <h2 className="text-xl font-bold text-white mb-4">Culturas Ativas</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {farmData.activeCrops.map((crop, index) => (
            <div key={index} className="bg-slate-900/50 rounded-lg p-4 border border-slate-700 hover:border-green-500/50 transition-all">
              <div className="flex items-center space-x-3">
                <div className="w-12 h-12 bg-gradient-to-br from-green-400 to-green-600 rounded-lg flex items-center justify-center text-white font-bold">
                  {crop[0]}
                </div>
                <div>
                  <h3 className="font-semibold text-white">{crop}</h3>
                  <p className="text-sm text-slate-400">Em produção</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <button className="bg-gradient-to-br from-blue-500/20 to-blue-600/20 hover:from-blue-500/30 hover:to-blue-600/30 backdrop-blur-lg rounded-xl p-6 border border-blue-500/30 transition-all text-left">
          <div className="w-12 h-12 bg-blue-500/30 rounded-lg flex items-center justify-center mb-4">
            <svg className="w-6 h-6 text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
            </svg>
          </div>
          <h3 className="text-white font-semibold mb-2">Monitorar Clima</h3>
          <p className="text-sm text-slate-400">Análise climática detalhada</p>
        </button>

        <button className="bg-gradient-to-br from-green-500/20 to-green-600/20 hover:from-green-500/30 hover:to-green-600/30 backdrop-blur-lg rounded-xl p-6 border border-green-500/30 transition-all text-left">
          <div className="w-12 h-12 bg-green-500/30 rounded-lg flex items-center justify-center mb-4">
            <svg className="w-6 h-6 text-green-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <h3 className="text-white font-semibold mb-2">Prever Produção</h3>
          <p className="text-sm text-slate-400">Estimativa de rendimento</p>
        </button>

        <button className="bg-gradient-to-br from-cyan-500/20 to-cyan-600/20 hover:from-cyan-500/30 hover:to-cyan-600/30 backdrop-blur-lg rounded-xl p-6 border border-cyan-500/30 transition-all text-left">
          <div className="w-12 h-12 bg-cyan-500/30 rounded-lg flex items-center justify-center mb-4">
            <svg className="w-6 h-6 text-cyan-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h3 className="text-white font-semibold mb-2">Irrigação</h3>
          <p className="text-sm text-slate-400">Otimizar uso de água</p>
        </button>

        <button className="bg-gradient-to-br from-purple-500/20 to-purple-600/20 hover:from-purple-500/30 hover:to-purple-600/30 backdrop-blur-lg rounded-xl p-6 border border-purple-500/30 transition-all text-left">
          <div className="w-12 h-12 bg-purple-500/30 rounded-lg flex items-center justify-center mb-4">
            <svg className="w-6 h-6 text-purple-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <h3 className="text-white font-semibold mb-2">Relatórios</h3>
          <p className="text-sm text-slate-400">Análise de desempenho</p>
        </button>
      </div>
    </div>
  )
}

export default Dashboard

