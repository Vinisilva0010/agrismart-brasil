import React, { useState } from 'react'

const ImageUpload = () => {
  const [selectedImage, setSelectedImage] = useState(null)
  const [preview, setPreview] = useState(null)
  const [cropType, setCropType] = useState('Soja')
  const [loading, setLoading] = useState(false)
  const [analysis, setAnalysis] = useState(null)

  const cropTypes = ['Soja', 'Milho', 'Café', 'Trigo', 'Cana-de-açúcar', 'Arroz', 'Feijão', 'Algodão']

  const handleImageSelect = (e) => {
    const file = e.target.files[0]
    if (file) {
      setSelectedImage(file)
      const reader = new FileReader()
      reader.onloadend = () => {
        setPreview(reader.result)
      }
      reader.readAsDataURL(file)
      setAnalysis(null)
    }
  }

  const analyzeImage = async () => {
    if (!selectedImage) return

    setLoading(true)
    setAnalysis(null)

    try {
      const formData = new FormData()
      formData.append('file', selectedImage)
      formData.append('crop_type', cropType)

      const response = await fetch('http://localhost:8080/api/crop/upload-image', {
        method: 'POST',
        body: formData,
      })

      const data = await response.json()
      setAnalysis(data)
    } catch (error) {
      console.error('Error analyzing image:', error)
      setAnalysis({
        status: 'error',
        error: 'Não foi possível conectar ao servidor. Verifique se a API está rodando.',
      })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Upload Section */}
        <div className="bg-slate-800/50 backdrop-blur-lg rounded-xl p-6 border border-slate-700">
          <h2 className="text-xl font-bold text-white mb-4">Análise de Cultura por Imagem</h2>

          {/* Crop Type Selection */}
          <div className="mb-4">
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Tipo de Cultura
            </label>
            <select
              value={cropType}
              onChange={(e) => setCropType(e.target.value)}
              className="w-full bg-slate-900/50 border border-slate-700 rounded-lg p-3 text-white focus:outline-none focus:border-green-500/50"
            >
              {cropTypes.map((type) => (
                <option key={type} value={type}>
                  {type}
                </option>
              ))}
            </select>
          </div>

          {/* Image Upload */}
          <div className="mb-4">
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Imagem da Cultura
            </label>
            <div className="relative">
              <input
                type="file"
                accept="image/*"
                onChange={handleImageSelect}
                className="hidden"
                id="image-upload"
              />
              <label
                htmlFor="image-upload"
                className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed border-slate-700 rounded-lg cursor-pointer hover:border-green-500/50 transition-all bg-slate-900/50"
              >
                {preview ? (
                  <img
                    src={preview}
                    alt="Preview"
                    className="w-full h-full object-contain rounded-lg"
                  />
                ) : (
                  <div className="flex flex-col items-center">
                    <svg
                      className="w-16 h-16 text-slate-500 mb-4"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                      />
                    </svg>
                    <p className="text-slate-400 mb-2">Clique para selecionar uma imagem</p>
                    <p className="text-sm text-slate-500">PNG, JPG ou JPEG até 10MB</p>
                  </div>
                )}
              </label>
            </div>
          </div>

          {/* Analyze Button */}
          <button
            onClick={analyzeImage}
            disabled={!selectedImage || loading}
            className="w-full px-6 py-3 bg-gradient-to-r from-green-500 to-blue-500 text-white rounded-lg font-medium hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? (
              <span className="flex items-center justify-center space-x-2">
                <svg className="animate-spin h-5 w-5" fill="none" viewBox="0 0 24 24">
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  ></circle>
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                  ></path>
                </svg>
                <span>Analisando...</span>
              </span>
            ) : (
              'Analisar Imagem'
            )}
          </button>

          {/* Features */}
          <div className="mt-6 space-y-3">
            <div className="flex items-start space-x-3">
              <div className="w-8 h-8 bg-green-500/20 rounded-lg flex items-center justify-center flex-shrink-0">
                <svg className="w-5 h-5 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <p className="text-white font-medium">Detecção de Doenças</p>
                <p className="text-sm text-slate-400">Identifica problemas na cultura</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-8 h-8 bg-blue-500/20 rounded-lg flex items-center justify-center flex-shrink-0">
                <svg className="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <div>
                <p className="text-white font-medium">Análise Nutricional</p>
                <p className="text-sm text-slate-400">Avalia deficiências de nutrientes</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-8 h-8 bg-purple-500/20 rounded-lg flex items-center justify-center flex-shrink-0">
                <svg className="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <div>
                <p className="text-white font-medium">Recomendações</p>
                <p className="text-sm text-slate-400">Sugestões de tratamento e prevenção</p>
              </div>
            </div>
          </div>
        </div>

        {/* Results Section */}
        <div className="bg-slate-800/50 backdrop-blur-lg rounded-xl p-6 border border-slate-700">
          <h2 className="text-xl font-bold text-white mb-4">Resultados da Análise</h2>

          {!analysis && !loading && (
            <div className="flex flex-col items-center justify-center h-96 text-slate-400">
              <svg className="w-24 h-24 mb-4 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              <p className="text-center">Selecione uma imagem e clique em "Analisar Imagem" para ver os resultados</p>
            </div>
          )}

          {loading && (
            <div className="flex flex-col items-center justify-center h-96">
              <div className="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-green-500 mb-4"></div>
              <p className="text-slate-400">Analisando imagem com IA...</p>
              <p className="text-sm text-slate-500 mt-2">Isso pode levar alguns segundos</p>
            </div>
          )}

          {analysis && analysis.status === 'error' && (
            <div className="bg-red-500/10 border border-red-500/30 rounded-lg p-6">
              <div className="flex items-center space-x-3 mb-3">
                <svg className="w-6 h-6 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <h3 className="text-lg font-semibold text-red-400">Erro na Análise</h3>
              </div>
              <p className="text-red-300">{analysis.error}</p>
            </div>
          )}

          {analysis && analysis.status === 'success' && (
            <div className="space-y-4 max-h-96 overflow-y-auto">
              <div className="bg-green-500/10 border border-green-500/30 rounded-lg p-4">
                <div className="flex items-center space-x-2 mb-2">
                  <svg className="w-5 h-5 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <h3 className="font-semibold text-green-400">Análise Concluída</h3>
                </div>
                <p className="text-sm text-slate-300">Cultura: {analysis.crop_type}</p>
              </div>

              <div className="bg-slate-900/50 rounded-lg p-4 border border-slate-700">
                <h4 className="font-semibold text-white mb-3">Resultados:</h4>
                <div className="prose prose-invert max-w-none">
                  <pre className="text-sm text-slate-300 whitespace-pre-wrap">{analysis.analysis}</pre>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Info Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-gradient-to-br from-green-500/20 to-green-600/20 backdrop-blur-lg rounded-xl p-6 border border-green-500/30">
          <div className="flex items-center space-x-3 mb-3">
            <div className="w-12 h-12 bg-green-500/30 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-green-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <h3 className="text-white font-semibold">IA Avançada</h3>
          </div>
          <p className="text-sm text-slate-300">Powered by Gemini 2.0 Flash para análises precisas</p>
        </div>

        <div className="bg-gradient-to-br from-blue-500/20 to-blue-600/20 backdrop-blur-lg rounded-xl p-6 border border-blue-500/30">
          <div className="flex items-center space-x-3 mb-3">
            <div className="w-12 h-12 bg-blue-500/30 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 className="text-white font-semibold">Rápido</h3>
          </div>
          <p className="text-sm text-slate-300">Resultados em segundos com alta precisão</p>
        </div>

        <div className="bg-gradient-to-br from-purple-500/20 to-purple-600/20 backdrop-blur-lg rounded-xl p-6 border border-purple-500/30">
          <div className="flex items-center space-x-3 mb-3">
            <div className="w-12 h-12 bg-purple-500/30 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-purple-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
              </svg>
            </div>
            <h3 className="text-white font-semibold">Acionável</h3>
          </div>
          <p className="text-sm text-slate-300">Recomendações práticas e implementáveis</p>
        </div>
      </div>
    </div>
  )
}

export default ImageUpload

