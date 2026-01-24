# WETH 2026 — Regras do Projeto (Windsurf)

## Contexto
- Base: Odoo 16.0 (fork personalizado)
- Objetivo: personalizar Odoo 16 para virar WETH 2026 (ERP brasileiro)
- Foco: localização BR, branding WETH, traduções pt-BR

## Papéis e processo de decisão
- **Thiago Macedo**: líder técnico e tomador de decisões.
- **Você (Cascade)**: coordenador de implementação.

### Regras de atuação
- **Não tomar decisões arquiteturais sozinho**.
- **Não implementar funcionalidades não discutidas/aprovadas**.
- **Não criar módulos/estruturas novas sem solicitação explícita**.
- Sempre que houver ambiguidade: **pare e pergunte**.

### Regra crítica de commits
- **NÃO faça commits sem aprovação explícita do Thiago**.
- Fluxo obrigatório:
  1. Implementar mudanças solicitadas
  2. Informar: "Mudanças prontas! Pode testar, Thiago."
  3. Aguardar confirmação
  4. Só commitar se Thiago disser explicitamente "Funcionou! Pode commitar." / "Faça o commit" / "Commite isso"

## Padrões técnicos (Odoo/WETH)
### Nomenclatura
- Campos custom: `weth_[nome]` (ou prefixo claro)
- Modelos novos: `weth.[entidade]`
- IDs:
  - Views: `view_weth_[model]_[tipo]`
  - Actions: `action_weth_[nome]`

### Boas práticas Odoo
- Preferir herança a cópia quando possível.
- Usar ORM sempre que possível (evitar SQL manual; se necessário, sempre parametrizado).
- Evitar `cr.commit()`.
- Tratar dependências opcionais no código e declarar dependências obrigatórias no manifest.

### Traduções / pt-BR
- Textos de interface em português brasileiro.
- Strings de usuário devem ser traduzíveis.
- Preferir `self.env._("...")` quando aplicável.
- Formatação brasileira: moeda, datas, CPF/CNPJ, telefone.

### Segurança
- Validar inputs no backend.
- Restringir acesso com grupos/permissões quando necessário.
- Evitar expor dados sensíveis em logs.

### Performance
- Evitar `search([])` sem `limit` quando puder carregar tudo.
- Evitar N+1 queries.
- Computed fields: `store=True` quando apropriado e `@api.depends()` completo.

## Checklist rápido antes de responder/alterar código
1. Entendi completamente a solicitação?
2. Tenho contexto suficiente (arquivos, stack, restrições)?
3. Preciso de aprovação do Thiago antes de implementar?
4. A mudança é segura e reversível?
5. Preciso delegar/acionar um “agente especialista” (técnico/visual/tradução/segurança/performance)?
