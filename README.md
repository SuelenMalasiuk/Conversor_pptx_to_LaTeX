# PPTX para LaTeX Beamer

Aplicação web desenvolvida em Python e Django para converter apresentações PowerPoint (`.pptx`) em código LaTeX Beamer, facilitando o reaproveitamento de conteúdo em apresentações acadêmicas.

## Sobre o projeto

O projeto surgiu com o objetivo de automatizar parte do processo de conversão de apresentações PowerPoint para LaTeX Beamer. A aplicação permite enviar um arquivo `.pptx` pela interface web e gerar um arquivo compactado com o código LaTeX e os recursos extraídos da apresentação.

## Funcionalidades

- Upload de apresentações no formato `.pptx`.
- Extração do conteúdo dos slides.
- Geração de código LaTeX Beamer.
- Extração das imagens utilizadas na apresentação.
- Download dos arquivos gerados em um arquivo ZIP.

## Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Django** — desenvolvimento da aplicação web.
- **python-pptx** — leitura e extração de conteúdo de apresentações PowerPoint.
- **PyLaTeX** — geração de código LaTeX.
- **HTML e CSS** — estrutura e estilização da interface.

## Estrutura do projeto

```text
Pptx_para_latex/
├── conversor/
│   ├── templates/
│   ├── conversor_pptx_para_latex.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── pptx_to_latex/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── iniciar.bat
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

### Pré-requisitos

- Python instalado no Windows.
- Pip disponível para instalar as dependências.

### Passo a passo

1. Clone o repositório ou baixe os arquivos do projeto.
2. Abra a pasta do projeto no computador.
3. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   ```bat
   venv\Scripts\activate
   ```

5. Instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Execute o arquivo `iniciar.bat` para iniciar a aplicação, caso ele esteja configurado para essa finalidade.

7. Acesse no navegador o endereço local indicado no terminal, normalmente:

   ```text
   http://127.0.0.1:8000/
   ```

## Observações

- A aplicação foi desenvolvida para trabalhar com arquivos PowerPoint no formato `.pptx`.
- O resultado da conversão pode exigir ajustes manuais, dependendo da estrutura e dos elementos utilizados na apresentação original.
- Recomenda-se testar a aplicação em um ambiente virtual Python.
- O suporte a elementos específicos do PowerPoint depende das funcionalidades implementadas no conversor.

## Autora

Projeto desenvolvido como parte da minha trajetória acadêmica em Ciência da Computação, com foco em Python, desenvolvimento web e automação da conversão de arquivos.
