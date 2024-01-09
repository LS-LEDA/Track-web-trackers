<template>
    <button @click="toggleSidebar" id="settings-btn">
        Toggle Sidebar
    </button>
    <div class="sidebar" :class="{ 'sidebar-open': isOpen }">
        <Accordion image="/search.svg" title="strings[language].customize">
          <ul>
            <li>Elemento 1</li>
            <li>Elemento 2</li>
            <li>Elemento 3</li>
          </ul>
        </Accordion>
    </div>
</template>
  
<script>
  import Accordion from './Accordion.vue';

  export default {
    data() {
        return {
          isOpen: false,
          language: 'en'
        };
    },
    methods: {
        toggleSidebar() {
          this.isOpen = !this.isOpen;
        },
    },
    components: { Accordion }
  };
</script>
  
  <style>

  :root {
    --sidebar-position: 1;
    --background-colour: #3498db;
  }
  .sidebar {
    position: fixed;
    top: 0;
    right: var(--sidebar-position); /**TODO: canviar la posició */
    height: calc(100vh - 20px);
    width: 300px;
    border-radius: 15px;
    margin: 10px;
    padding: 20px;
    background-color: #ffff;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.4);
    transition: transform 0.3s ease;
    transform: translateX(-110%);
  }
  
  .sidebar-open {
    transform: translateX(0);
  }
  
  #settings-btn {
    margin: 10px;
    padding: 8px;
    background-color: #3498db;
    color: #fff;
    border: none;
    cursor: pointer;
  }
  </style>
  