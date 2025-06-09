# Documentação do Projeto: Projeto Smart Plan

## 1. Visão Geral
**Tecnologia Utilizada:**

* Python
* FastAPI
* Uvicorn

**Descrição:** o SmartPlan é um sistema web com o objetivo de apoiar estudantes do ensino médio e de cursinhos pré-vestibulares na preparação para o ENEM e vestibulares, no contexto de organização de estudo e de tempo.
  
**Objetivo:** O objetivo geral desta pesquisa é projetar, implementar e avaliar o SmartPlan como uma ferramenta de apoio à preparação para exames, promovendo maior organização, autonomia e eficácia no processo de aprendizagem.

***

## 2. Descrição Detalhada do Projeto

### O que é o projeto?

A proposta busca oferecer uma plataforma intuitiva, que reúna funcionalidades voltadas à gestão do tempo, organização de conteúdos e suporte educacional personalizado, promovendo uma experiência de aprendizagem mais eficiente e acessível. A opção por uma solução web justifica-se por sua ampla acessibilidade, permitindo que estudantes de diferentes regiões e contextos sociais utilizem o sistema a partir de dispositivos conectados à internet, sem a exigência de equipamentos de alto desempenho.

### 2.1 Funcionalidades Principais

**Funcionalidade 01:** Simular notas de corte do Enem.
  * Permite ao estudante simular sua colocação com base nas notas obtidas.
  * Considera notas reais ou estimadas em cada área do conhecimento.
  * Compara os dados com notas de corte de cursos e instituições para auxiliar na tomada de decisão.
    
**Funcionalidade 02:** Filtro de questões personalizado.
  * O sistema oferece uma base de dados com questões categorizadas por:
    * Matéria
    * Assunto
    * Dificuldade
    * Status (feita ou não pelo usuário)
  * Os usuários podem montar listas de estudo filtrando as questões conforme suas necessidades.
    
**Funcionalidade 03:** Login e Cadastro de usuário
  * Permite que cada usuário tenha seu próprio perfil com progresso salvo.
  * Permite registrar estatísticas individuais, como questões resolvidas, listas salvas e simulações feitas.

### 2.2 Arquitetura do Código
```
Smartplan/  
├── main.py            # Ponto de entrada (inicialização)  
├── api.py             # Lógica da API   
├── models.py          # Modelos com Pydantic
├── db_smartplan.sql   # Banco de Dados MySQL
├── diagrama.pdf       # Digramas do Banco de Dados
├── README.md          # Documentação   
├── requirements.txt   # Requisitos para instalação
```

## 3. Etapas de Entrega (Cronograma Detalhado)

### Etapa 1:  Requisitos do Sistema
### Etapa 2:  Diagramas de Caso de Uso  
### Etapa 3:  Criação de Banco de Dados 
### Etapa 4:  Revisão das Etapas anteriores e possíveis alterações 
### Etapa 5:  Construças da API 
