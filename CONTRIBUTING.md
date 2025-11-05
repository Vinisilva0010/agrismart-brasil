# 🤝 Guia de Contribuição

Obrigado por considerar contribuir com o AgriSmart Brasil! Este documento fornece diretrizes para contribuir com o projeto.

## 📋 Código de Conduta

Ao participar deste projeto, você concorda em seguir nosso código de conduta:

- Seja respeitoso e inclusivo
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Mostre empatia com outros membros da comunidade

## 🚀 Como Contribuir

### 1. Reportar Bugs

Se você encontrar um bug, por favor crie uma issue incluindo:

- **Descrição clara** do problema
- **Passos para reproduzir** o erro
- **Comportamento esperado** vs **comportamento atual**
- **Screenshots** (se aplicável)
- **Ambiente** (SO, versão do Python/Node, etc.)

### 2. Sugerir Melhorias

Para sugerir uma nova funcionalidade:

- Crie uma issue com a tag `enhancement`
- Descreva a funcionalidade desejada
- Explique por que ela seria útil
- Forneça exemplos de uso, se possível

### 3. Contribuir com Código

#### Setup do Ambiente de Desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/yourusername/agrismart-brasil.git
cd agrismart-brasil

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
```

#### Processo de Contribuição

1. **Fork** o repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Faça suas alterações** seguindo os padrões do projeto
4. **Teste** suas alterações
5. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
6. **Push** para a branch (`git push origin feature/AmazingFeature`)
7. **Abra um Pull Request**

#### Padrões de Código

**Python (Backend)**
- Siga [PEP 8](https://pep8.org/)
- Use type hints
- Docstrings para funções e classes
- Máximo 100 caracteres por linha

```python
def example_function(param: str) -> Dict[str, Any]:
    """
    Brief description of the function.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    return {"result": param}
```

**JavaScript/React (Frontend)**
- Use ESLint configurado no projeto
- Componentes funcionais com hooks
- PropTypes ou TypeScript para validação
- 2 espaços para indentação

```javascript
const ExampleComponent = ({ prop1, prop2 }) => {
  const [state, setState] = useState(null)
  
  return (
    <div>
      {/* Component content */}
    </div>
  )
}

export default ExampleComponent
```

#### Commits

Use mensagens de commit descritivas seguindo o padrão:

```
tipo: descrição curta

Descrição mais detalhada (opcional)

Closes #issue_number
```

Tipos:
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação, ponto e vírgula faltando, etc
- `refactor`: Refatoração de código
- `test`: Adição de testes
- `chore`: Atualização de tarefas, etc

Exemplos:
```
feat: adicionar agente de previsão de pragas

fix: corrigir erro no upload de imagens

docs: atualizar guia de instalação
```

### 4. Pull Requests

Ao abrir um PR:

- **Descreva** o que foi alterado e por quê
- **Referencie** issues relacionadas
- **Inclua screenshots** se houver mudanças visuais
- **Garanta** que todos os testes passam
- **Atualize** a documentação se necessário

Template de PR:

```markdown
## Descrição
Breve descrição das mudanças

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## Checklist
- [ ] Testei localmente
- [ ] Atualizei a documentação
- [ ] Segui os padrões de código
- [ ] Adicionei testes (se aplicável)

## Screenshots (se aplicável)
```

## 🧪 Testes

### Backend

```bash
cd backend
pytest tests/
```

### Frontend

```bash
cd frontend
npm test
```

## 📝 Documentação

- Documente novas funcionalidades no README
- Atualize o DEPLOYMENT.md se houver mudanças no processo de deploy
- Comente código complexo
- Mantenha exemplos de uso atualizados

## 🏗️ Estrutura de Branches

- `main`: Código de produção estável
- `develop`: Branch de desenvolvimento
- `feature/*`: Novas funcionalidades
- `fix/*`: Correções de bugs
- `docs/*`: Atualizações de documentação

## 🎯 Prioridades de Desenvolvimento

Áreas que precisam de contribuição:

1. **Testes**: Aumentar cobertura de testes
2. **Documentação**: Melhorar exemplos e guias
3. **Performance**: Otimizações e melhorias
4. **Novos Agentes**: Implementar agentes especializados
5. **UI/UX**: Melhorias na interface
6. **Internacionalização**: Suporte a múltiplos idiomas

## 💬 Comunicação

- **Issues**: Para bugs e sugestões
- **Discussions**: Para perguntas e discussões gerais
- **Pull Requests**: Para contribuições de código

## 📚 Recursos

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [Google AI Docs](https://ai.google.dev/docs)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)

## ❓ Dúvidas?

Se tiver dúvidas sobre como contribuir:

1. Verifique a documentação existente
2. Procure em issues fechadas
3. Abra uma discussion
4. Entre em contato com os mantenedores

## 🎉 Reconhecimento

Todos os contribuidores serão reconhecidos no README do projeto!

---

Obrigado por contribuir com o AgriSmart Brasil! 🌾

