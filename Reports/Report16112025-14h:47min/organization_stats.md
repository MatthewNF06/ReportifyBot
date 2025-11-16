# 📈 GitHub Issue Stats - Organização

| 🟢 Abertas | 🔴 Fechadas | 📦 Total | ✅ % Fechadas |
|----------|------------|---------|------------|
| 5 | 10 | 15 | 66.7% |


---
## 📊 Entregas Quinzenais da Organização

![Organization biweekly chart](/organization_charts/organization_biweekly.png)

**Velocidade média quinzenal:** 3.33 issues/quinzena

| Período | Prometido | Entregue | % Concluído | Velocidade |
|--------|------------|----------|--------------|------------|
| 2025-09-22 | 6 | 3 | 50.0% | 3 |
| 2025-10-06 | 3 | 2 | 66.7% | 2 |
| 2025-10-27 | 6 | 5 | 83.3% | 5 |

## 🔥 Burn-up Chart da Organização

![Organization burnup chart](/organization_charts/organization_burnup.png)

## 🎲 Simulação Monte Carlo

![Organization monte carlo simulation](/organization_charts/organization_monte_carlo.png)

![Organization velocity distribution](/organization_charts/organization_velocity_dist.png)

### Previsões de Velocidade e Conclusão da Organização

| Métrica | Valor |
|--------|-------|
| Velocidade Média | 3.37 issues/quinzena |
| Velocidade P10 (Otimista) | 2.36 issues/quinzena |
| Velocidade P50 (Provável) | 3.28 issues/quinzena |
| Velocidade P90 (Conservador) | 4.52 issues/quinzena |
| Data de Conclusão P10 (Otimista) | 2025-11-11 |
| Data de Conclusão P50 (Provável) | 2025-11-17 |
| Data de Conclusão P90 (Conservador) | 2025-11-25 |

### Explicação da Simulação Monte Carlo

| Conceito | Explicação |
|---------|------------|
| **O que é Monte Carlo?** | Técnica estatística que utiliza amostragens aleatórias repetidas para obter resultados numéricos e estimar probabilidades. |
| **Como funciona a simulação?** | 1) Coletamos o histórico de velocidade da organização (issues concluídas/semana)<br>2) Fazemos 1000 simulações com variações aleatórias dessas velocidades<br>3) Para cada simulação, calculamos quando o trabalho restante seria concluído<br>4) Organizamos os resultados e calculamos os percentis |
| **O que significa P10?** | Cenário otimista. Existe apenas 10% de chance de concluir o trabalho antes desta data. É um resultado rápido e favorável, mas menos provável. |
| **O que significa P50?** | Cenário mais provável. 50% de chance de terminar antes ou depois desta data. É nossa melhor estimativa 'realista'. |
| **O que significa P90?** | Cenário conservador. Existe 90% de chance de concluir antes desta data. Útil para planejamento seguro, pois é improvável atrasar além deste ponto. |
| **Por que usar Monte Carlo?** | Fornece intervalos de confiança em vez de datas únicas, reconhecendo a incerteza natural no desenvolvimento. Captura a variabilidade histórica da organização. |
| **Como interpretar velocidades?** | Quanto maior a velocidade, mais rápido a organização conclui issues. P10/P50/P90 para velocidades mostram diferentes cenários de produtividade que usamos nos cálculos. |
| **Contexto dos dados** | Com base nos dados históricos, a organização tem volatilidade moderada (alguma variação na entrega). A diferença entre o cenário otimista e conservador é de 14 dias. Os dados são confiáveis para planejamento. Recomendamos usar P50 (2025-11-17) para comunicação de prazos. |
