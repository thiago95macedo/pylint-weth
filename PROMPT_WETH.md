# Prompt para IA - Uso do pylint-weth no Projeto WETH

## 🎯 CONTEXTO DO PROJETO

**WETH** é um ERP brasileiro personalizado baseado no Odoo 16.0, desenvolvido com foco em:
- Localização brasileira completa
- Identidade visual WETH (#05285B)
- Traduções nativas em português brasileiro
- Padrões de desenvolvimento específicos

## 🧭 USO COM WINDSURF / CASCADE

- As regras de projeto para o Cascade (Windsurf) ficam em `/.windsurf/rules/weth.md`.
- Ao iniciar uma tarefa, siga essas regras (principalmente: processo de decisão com o Thiago e **não commitar sem aprovação**).

## 🔧 CONFIGURAÇÃO DO PYLINT-WETH

### Instalação
```bash
# Instalar o plugin pylint-weth
pip install pylint-weth

# Ou instalar em modo desenvolvimento
pip install -e /caminho/para/pylint-weth
```

### Configuração (.pylintrc)
O arquivo `.pylintrc` já está configurado na raiz do projeto WETH com:
- Plugin `pylint_weth` carregado
- Verificações WETH habilitadas (`wethlint`)
- Verificações desnecessárias desabilitadas
- Padrões otimizados para desenvolvimento WETH

## 📋 COMO USAR O PYLINT-WETH

### 1. Uso Básico
```bash
# Analisar módulo específico
pylint addons/module_name/

# Analisar todos os módulos WETH
pylint addons/

# Apenas verificações WETH (recomendado)
pylint --disable=all --enable=wethlint addons/module_name/
```

### 2. Uso com Arquivo de Configuração
```bash
# Usar configuração do .pylintrc automaticamente
pylint addons/module_name/

# Forçar uso de configuração específica
pylint --rcfile=.pylintrc addons/module_name/
```

### 3. Integração com IDE
```bash
# Para VS Code, adicionar ao settings.json:
{
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_weth",
        "--disable=all",
        "--enable=wethlint"
    ]
}
```

## 🎯 PRINCIPAIS VERIFICAÇÕES WETH

### 🔒 Segurança
- **SQL Injection**: Detecta vulnerabilidades de injeção SQL
- **Validação de Inputs**: Verifica validação adequada de dados
- **Controle de Acesso**: Valida permissões e grupos de segurança

### 📋 Manifest e Estrutura
- **Manifest válido**: Verifica estrutura do `__manifest__.py`
- **Versão correta**: Valida formato de versão (2026.0.x.y.z)
- **Dependências**: Verifica dependências declaradas
- **Licença**: Valida licença especificada

### 🌐 Traduções
- **Strings traduzíveis**: Detecta textos não traduzidos
- **Métodos de tradução**: Verifica uso correto de `_()` e `self.env._()`
- **Formatação**: Valida formatação de strings de tradução
- **Lazy loading**: Verifica uso de lazy loading em traduções

### 🏗️ Arquitetura WETH
- **Métodos deprecated**: Detecta uso de APIs antigas
- **Herança**: Valida herança correta de modelos
- **Campos computed**: Verifica métodos compute adequados
- **Workflows**: Valida transições de estado

## 🚀 MELHORIAS E OTIMIZAÇÕES

### 1. Correção Automática de Problemas Comuns

#### SQL Injection
```python
# ❌ PROBLEMA: SQL Injection
query = f"SELECT * FROM table WHERE id = {user_id}"

# ✅ SOLUÇÃO: Query parametrizada
query = "SELECT * FROM table WHERE id = %s"
self.env.cr.execute(query, (user_id,))

# ✅ MELHOR: Usar ORM do WETH
records = self.env['model.name'].search([('id', '=', user_id)])
```

#### Traduções
```python
# ❌ PROBLEMA: String não traduzida
message = "Erro ao processar dados"

# ✅ SOLUÇÃO: Usar método de tradução
message = self.env._("Erro ao processar dados")
```

#### Métodos Deprecated
```python
# ❌ PROBLEMA: Método deprecated
def name_get(self):
    return [(record.id, record.name) for record in self]

# ✅ SOLUÇÃO: Usar _compute_display_name
def _compute_display_name(self):
    for record in self:
        record.display_name = record.name
```

### 2. Padrões de Código WETH

#### Estrutura de Modelo
```python
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class WethModel(models.Model):
    """Modelo para [descrição em português]."""
    
    _name = 'weth.model'
    _description = 'Modelo WETH'
    _order = 'create_date desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(
        string='Nome',
        required=True,
        tracking=True,
        help='Nome do registro'
    )
    
    @api.constrains('name')
    def _check_name(self):
        """Valida o campo name."""
        for record in self:
            if not record.name:
                raise ValidationError(_('Nome é obrigatório!'))
```

#### Estrutura de Views
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Form View -->
    <record id="view_weth_model_form" model="ir.ui.view">
        <field name="name">weth.model.form</field>
        <field name="model">weth.model</field>
        <field name="arch" type="xml">
            <form string="[Título em PT-BR]">
                <header>
                    <button name="action_confirm" string="Confirmar"
                        type="object" class="oe_highlight"
                        states="draft"/>
                    <field name="state" widget="statusbar"/>
                </header>
                <sheet>
                    <group>
                        <group>
                            <field name="name"/>
                        </group>
                    </group>
                </sheet>
                <div class="oe_chatter">
                    <field name="message_follower_ids"/>
                    <field name="message_ids"/>
                </div>
            </form>
        </field>
    </record>
</odoo>
```

### 3. Integração com Pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/PyCQA/pylint
    rev: v3.0.1
    hooks:
      - id: pylint
        args: [--load-plugins=pylint_weth]
```

### 4. CI/CD Integration

```yaml
# .github/workflows/lint.yml
name: Lint WETH Code
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install pylint-weth
      - name: Run pylint-weth
        run: |
          pylint --load-plugins=pylint_weth --disable=all --enable=wethlint addons/
```

## 📊 INTERPRETAÇÃO DE RESULTADOS

### Códigos de Erro
- **E**: Error (erro crítico)
- **W**: Warning (aviso)
- **C**: Convention (convenção)
- **R**: Refactor (refatoração)

### Exemplos de Saída
```
addons/weth_module/models/model.py:45: [E8103(sql-injection), Model.method] SQL injection risk. Use parameters if you can.
addons/weth_module/models/model.py:67: [W8161(prefer-env-translation), Model.method] Better using self.env._ More info at https://github.com/weth/weth/pull/174844
addons/weth_module/models/model.py:89: [C8108(method-compute), Model] Name of compute method should start with "_compute_"
```

## 🎯 CHECKLIST DE QUALIDADE

### ✅ Antes de Commitar
- [ ] Executar `pylint --disable=all --enable=wethlint addons/modulo/`
- [ ] Corrigir todos os erros (E) e warnings (W)
- [ ] Verificar traduções em português
- [ ] Validar estrutura do manifest
- [ ] Testar funcionalidades básicas

### ✅ Padrões WETH
- [ ] Strings em português brasileiro
- [ ] Documentação em português
- [ ] Uso correto de `self.env._()` para traduções
- [ ] Validações com `@api.constrains`
- [ ] Herança correta de modelos

## 🚨 PROBLEMAS COMUNS E SOLUÇÕES

### 1. "SQL injection risk"
```python
# ❌ Problema
query = f"SELECT * FROM table WHERE id = {id}"

# ✅ Solução
query = "SELECT * FROM table WHERE id = %s"
self.env.cr.execute(query, (id,))
```

### 2. "Better using self.env._"
```python
# ❌ Problema
message = _("Texto")

# ✅ Solução
message = self.env._("Texto")
```

### 3. "Missing required key in manifest"
```python
# ❌ Problema: Manifest incompleto
{
    'name': 'Módulo',
    'version': '2026.0.1.0.0',
}

# ✅ Solução: Manifest completo
{
    'name': 'WETH - Módulo',
    'version': '2026.0.1.0.0',
    'author': 'WETH',
    'website': 'https://www.weth.com.br',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': ['views/views.xml'],
    'installable': True,
}
```

## 📈 MELHORIAS CONTÍNUAS

### 1. Monitoramento de Qualidade
- Executar pylint-weth regularmente
- Acompanhar métricas de qualidade
- Identificar padrões de problemas
- Treinar equipe nos padrões WETH

### 2. Customizações Específicas
- Adicionar verificações específicas do negócio
- Configurar thresholds de qualidade
- Integrar com ferramentas de CI/CD
- Automatizar correções quando possível

### 3. Documentação e Treinamento
- Manter documentação atualizada
- Treinar desenvolvedores nos padrões
- Criar exemplos de código correto
- Compartilhar melhores práticas

---

## 🎯 RESUMO PARA IA

**SEMPRE que trabalhar com código WETH:**

1. **Execute pylint-weth** antes de sugerir mudanças
2. **Corrija problemas de segurança** (SQL injection, validações)
3. **Use traduções corretas** (`self.env._()` em português)
4. **Siga padrões WETH** (prefixos, estrutura, documentação)
5. **Valide manifest** (versão 2026.0.x.y.z, campos obrigatórios)
6. **Mantenha qualidade** (documentação, testes, validações)

**O pylint-weth é sua ferramenta principal para garantir qualidade e segurança no código WETH!**
