# pylint-weth

Plugin Pylint especializado para análise de código de módulos WETH.

## Descrição

O `pylint-weth` é um plugin do Pylint que fornece verificações especializadas para desenvolvimento de módulos WETH, garantindo qualidade de código, segurança e conformidade com as melhores práticas.

## Instalação

```bash
pip install pylint-weth
```

## Uso

### Básico
```bash
pylint --load-plugins=pylint_weth src/
```

### Com arquivo de configuração
```bash
pylint --rcfile=.pylintrc src/
```

### Apenas verificações WETH
```bash
pylint --load-plugins=pylint_weth -d all -e wethlint src/
```

## Principais Verificações

### 🔒 Segurança
- **SQL Injection**: Detecta vulnerabilidades de injeção SQL
- **Validação de Inputs**: Verifica validação adequada de dados
- **Controle de Acesso**: Valida permissões e grupos de segurança

### 📋 Manifest e Estrutura
- **Manifest válido**: Verifica estrutura do `__manifest__.py`
- **Versão correta**: Valida formato de versão (16.0.x.y.z)
- **Dependências**: Verifica dependências declaradas
- **Licença**: Valida licença especificada

### 🌐 Traduções
- **Strings traduzíveis**: Detecta textos não traduzidos
- **Métodos de tradução**: Verifica uso correto de `_()` e `_lt()`
- **Formatação**: Valida formatação de strings de tradução

### 🏗️ Arquitetura
- **Imports relativos**: Detecta imports absolutos desnecessários
- **Métodos deprecated**: Identifica uso de métodos obsoletos
- **Herança**: Valida estrutura de herança de modelos
- **Workflows**: Verifica transições de estado

### 📊 Qualidade de Código
- **Nomenclatura**: Valida nomes de variáveis e métodos
- **Complexidade**: Detecta código complexo demais
- **Duplicação**: Identifica código duplicado
- **Documentação**: Verifica docstrings e comentários

## Configuração

### Arquivo `.pylintrc`
```ini
[MASTER]
load-plugins=pylint_weth

[MESSAGES CONTROL]
disable=all
enable=wethlint,pointless-statement,trailing-newlines

[wethlint]
manifest-required-authors=WETH
license-allowed=LGPL-3,AGPL-3
```

### Pre-commit Hook
```yaml
repos:
  - repo: https://github.com/thiago95macedo/pylint-weth
    rev: main
    hooks:
      - id: pylint_weth
```

## Exemplos de Problemas Detectados

### SQL Injection
```python
# ❌ Problema detectado
query = f"SELECT * FROM res_partner WHERE name = '{name}'"

# ✅ Solução recomendada
query = "SELECT * FROM res_partner WHERE name = %s"
```

### Tradução
```python
# ❌ Problema detectado
message = "User created successfully"

# ✅ Solução recomendada
message = _("User created successfully")
```

### Manifest
```python
# ❌ Problema detectado
{
    'name': 'My Module',
    'version': '1.0.0',  # Formato incorreto
}

# ✅ Solução recomendada
{
    'name': 'My Module',
    'version': '16.0.1.0.0',  # Formato correto
}
```

## Integração com CI/CD

### GitHub Actions
```yaml
name: Lint WETH Modules
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install pylint-weth
      - name: Run pylint
        run: |
          pylint --load-plugins=pylint_weth src/
```

## Desenvolvimento

### Instalação para desenvolvimento
```bash
git clone https://github.com/thiago95macedo/pylint-weth.git
cd pylint-weth
pip install -e .
```

### Executar testes
```bash
python -m pytest tests/
```

### Executar linting
```bash
pylint --load-plugins=pylint_weth src/
```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença AGPL-3.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Suporte

- **Issues**: [GitHub Issues](https://github.com/thiago95macedo/pylint-weth/issues)
- **Documentação**: [Wiki do projeto](https://github.com/thiago95macedo/pylint-weth/wiki)

## WETH

Este plugin é desenvolvido especificamente para o projeto **WETH**, uma personalização do Odoo 16 focada no mercado brasileiro.

- **Website**: https://www.weth.com.br
- **Documentação**: https://docs.weth.com.br