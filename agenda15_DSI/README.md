# 👾 DOUGVADERS GAMEDEV — Portfólio Pessoal

**Aluno:** Douglas Leonardo dos Santos

**GitHub:** [@doug-79](https://github.com/doug-79)

**Repositório:** https://github.com/doug-79/trabalhos_etec

**Site publicado (GitHub Pages):** COLOQUE_AQUI_O_LINK_DO_SITE

---

## 📋 Descrição do Portfólio

O **DOUGVADERS GAMEDEV** é um portfólio pessoal com identidade visual retrô, inspirado nos fliperamas clássicos da era 8-bit.

O site foi desenvolvido para apresentar minha trajetória no desenvolvimento de jogos independentes, reunindo informações sobre meu perfil, projetos desenvolvidos e canais de contato.

A proposta é compartilhar meus trabalhos, experiências e aprendizados na área de desenvolvimento de games.

---

## 🛠️ Tecnologias Utilizadas

- **HTML5:** Estruturação do conteúdo e das seções da página.
- **CSS3:** Estilização personalizada, cores neon, tipografia retrô, animações e efeitos visuais.
- **Bootstrap 5.3.3:** Utilizado na construção do carrossel de projetos.
- **JavaScript:** Utilizado pelo Bootstrap para controlar as funcionalidades do carrossel.

---

## ⚙️ Funcionamento do Projeto

O portfólio funciona como uma página única, dividida em três seções principais:

1. **Perfil:** Apresentação pessoal, interesses e tecnologias relacionadas ao desenvolvimento de jogos.
2. **Projetos:** Exibição de três projetos: Dougvaders, Jogo da Velha e Mata Rato.
3. **Contatos:** Disponibiliza links para GitHub, Itch.io e endereço de e-mail.

O menu de navegação permite acessar diretamente cada seção por meio de links internos.

O carrossel apresenta imagens dos projetos e permite navegar entre elas utilizando os controles de avançar e retroceder.

---

## ✨ Recurso Novo Adicionado

Além da estrutura desenvolvida em aula, foram adicionados recursos para melhorar a aparência e a navegação do portfólio:

- **Rolagem suave (Smooth Scroll):** A navegação entre as seções acontece com um deslizamento suave da página.
- **Efeitos Hover Neon:** Os links do menu e de contato mudam de cor e recebem um efeito luminoso quando o mouse passa sobre eles.
- **Personalização do Carrossel:** As imagens possuem tamanho padronizado e utilizam ajuste automático para evitar cortes e deformações.

---

## 💻 Explicação da Implementação do Recurso Novo

### 1. Rolagem suave

No arquivo `css/style.css`, foi utilizada a propriedade:

```css
html {
    scroll-behavior: smooth;
}
```

Essa propriedade faz com que a página deslize suavemente até a seção selecionada no menu.

### 2. Efeitos Hover Neon

Foram utilizados os seletores `:hover`, `transition` e `text-shadow` para criar efeitos luminosos nos links.

Exemplo:

```css
.menu-topo a:hover {
    color: #00ff66;
    text-shadow: 0 0 8px #00ff66;
}
```

O mesmo efeito foi aplicado aos links de contato por meio da classe `.link-contato:hover`.

### 3. Personalização do Carrossel

Para manter as imagens dos jogos organizadas, foi utilizado:

```css
.carousel-item img {
    height: 450px;
    object-fit: contain;
    background-color: #000;
}
```

A propriedade `object-fit: contain` mantém a proporção original das imagens, evitando cortes e deformações.

---

## 📁 Organização dos Arquivos

- `index.html` — Estrutura principal do site.
- `css/style.css` — Estilos personalizados.
- `css/bootstrap.min.css` — Estilos do Bootstrap.
- `js/bootstrap.bundle.min.js` — Funcionalidades JavaScript do Bootstrap.
- `image/` — Imagens utilizadas nos projetos.

---

**Desenvolvido por Douglas Leonardo dos Santos**

👾 DOUGVADERS GAMEDEV — Do código ao jogo!