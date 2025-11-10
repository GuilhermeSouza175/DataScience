
# Análise de Dados Ambientais para Soluções Sustentáveis nas Cidades

## 1. Introdução
Este relatório documenta o projeto acadêmico **Análise de Dados Ambientais para Soluções Sustentáveis nas Cidades**, cujo objetivo é aplicar o ciclo de vida da ciência de dados e propor soluções práticas para desafios urbanos relacionados a energia, qualidade do ar, resíduos e uso de recursos.

## 2. Ciclo de Vida da Ciência de Dados Aplicado
1. **Entendimento do problema**: identificar fontes de impacto ambiental em áreas urbanas (consumo energético, poluentes, resíduos, uso de água e solos);
2. **Coleta de dados**: conjuntos sobre consumo energético, qualidade do ar, produção de resíduos e uso de recursos naturais;
3. **Preparação dos dados**: limpeza, normalização, tratamento de datas e valores faltantes;
4. **Análise exploratória**: estatísticas descritivas, séries temporais, detecção de outliers e correlações;
5. **Modelagem**: (opcional) modelos preditivos para consumo energético ou previsão de qualidade do ar;
6. **Comunicação**: elaboração de relatórios, painéis (Power BI) e apresentação oral com visualizações.

## 3. Metodologia de Limpeza e Organização de Dados
- Normalização de nomes de colunas (lowercase, underscores);
- Conversão de colunas de data para datetime;
- Substituição de strings vazias por NaN e imputação quando necessário (média, mediana, forward-fill);
- Tratamento de outliers via IQR e análise de caso a caso;
- Verificação de consistência entre variáveis (ex.: soma de categorias = total).

## 4. Análise de Padrões e Anomalias (Procedimentos)
- Análise de séries temporais para identificar tendências e sazonalidade;
- Decomposição temporal (trend/seasonal/residual) quando aplicável;
- Correlação entre consumo energético e temperatura/ocupação;
- Verificação de picos em poluentes (PM2.5, PM10, NO₂) e cruzamento com eventos (queima, tráfego intenso);
- Identificação de bairros com maior geração de resíduos por habitante.

## 5. Insights e Aplicações Práticas (Exemplos)
- **Eficiência energética por bairro**: identificar horários de pico para implantação de tarifas diferenciadas ou programas de eficiência.
- **Zonas críticas de poluição**: priorizar instalação de barreiras verdes, restrição de tráfego e monitoramento em tempo real.
- **Reciclagem direcionada**: implementar programas de coleta seletiva em bairros com maior geração de resíduos orgânicos/recicláveis.
- **Uso de recursos hídricos**: detectar desperdícios por setor e promover campanhas e tecnologias de reúso.

## 6. Soluções Propostas (Prós / Contras)
- **Energia renovável (ex.: painéis solares)**: reduz emissões; alto custo inicial e necessidade de incentivos.
- **Melhoria do sistema de coleta de resíduos**: reduz poluição; exige mudança comportamental e investimentos em logística.
- **Políticas públicas integradas**: escala maior de impacto; podem enfrentar resistência política e necessidade de financiamento.

## 7. Barreiras e Recomendações
- Barreiras: custo, infraestrutura, governança e aceitação pública.
- Recomendações: projetos-piloto, parcerias público-privadas, campanhas educativas e uso de indicadores (KPIs) para monitoramento.

## 8. Conclusão
O uso de ciência de dados para problemas urbanos ambientais permite priorizar ações, maximizar impacto com recursos limitados e criar políticas baseadas em evidências.

---
## Anexos: Gráficos Gerados
Os gráficos gerados pela seção prática (código Python) ficam salvos na pasta **outputs/**. Exemplos de imagens esperadas:
- consumo_medio_mes.png
- poluentes_timeseries.png
- residuo_top10_bairro.png
- uso_recursos_relativo.png
