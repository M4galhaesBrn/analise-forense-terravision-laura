# analise-forense-terravision-laura
## Identificação

**Aluno:** Laura Bruna Magalhães Silva
**Turma:** 3º D — DS
**Disciplinas:** Ciência de Dados e Computação Gráfica
**Tema:** Regiões Vulcânicas e Formações Geológicas Ativas

---

# Etapa 1 — Ciência de Dados e Lógica

Foi desenvolvida uma função em Python chamada `carregar_camada_satelite(lista_altitudes)`.

A função recebe uma lista de altitudes e utiliza estruturas condicionais para determinar qual nível de resolução deve ser carregado.

- Altitude acima de 10.000 m: baixa resolução.
- Altitude entre 1.000 m e 10.000 m: média resolução.
- Altitude abaixo de 1.000 m: alta resolução.

No meu tema, as camadas de alta resolução permitem visualizar com maior detalhe elementos como crateras, cones vulcânicos e outras formações geológicas.

---

# Etapa 2 — Computação Gráfica e UX/UI

## 1. Processamento e Tratamento de Imagem

Na representação de regiões vulcânicas, um dos desafios é trabalhar com as diferenças de iluminação e sombra causadas pelo relevo acentuado. Essas diferenças podem dificultar a visualização das crateras e das formas do terreno.

Outro desafio é a diferença de cores e texturas entre áreas com neve, rochas e vegetação. O processamento das imagens precisa manter essas características visuais de maneira uniforme durante a aproximação do usuário.

Também pode existir dificuldade na costura das imagens de satélite, principalmente quando diferentes imagens apresentam variações de iluminação, cor ou resolução.

## 2. Design de Interface e Leis da Gestalt

### Figura-Fundo

A Lei da Figura-Fundo pode ser observada na interface porque o usuário consegue diferenciar o terreno e as formações geológicas dos elementos de navegação e informações exibidos na tela.

Isso facilita a identificação do Monte Fuji e permite que o usuário concentre sua atenção no relevo.

### Continuidade

A Lei da Continuidade aparece na forma como o usuário acompanha o relevo enquanto realiza a aproximação do mapa.

A continuidade das formas do terreno ajuda o usuário a compreender a estrutura da região e facilita a navegação durante o zoom.

O design da interface também orienta a atenção por meio dos nomes dos locais e dos elementos visuais apresentados sobre o mapa.

## 3. Imagem/Evidência

A imagem abaixo apresenta uma captura do Google Earth mostrando o Monte Fuji, uma formação vulcânica, e seu relevo.

![Monte Fuji no Google Earth](monte-fuji.jpg)
