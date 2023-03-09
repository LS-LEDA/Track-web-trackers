# LS-web-trackers

The project is an user rights of control initiative to expose web trackers and raise awareness regarding automatic data collection.

The Internet has become, against the user community's desire, a capitalist surveillance digital space with no privacy and merci. Websites use cookies, third-party APIs, and other techy mechanisms to collect different kinds of data from Internet users for economic purposes. These data collectors transform data into users' behaviors and habits, which are fully observed and aggregated through code snippets hidden among websites' code. These third-party actors are considered 'trackers' and allow user profiling to display targeted advertising and sell behavioral profiles to multiple companies for purposes that violate community rights. Transparency is required regarding the use of trackers so that users gain awareness about who is taking data from them on a website and thus make better-informed decisions to avoid surveillance mechanisms. Hence, Internet users need tools to protect themselves from trackers. The project aims to help build a more transparent Internet by exposing web trackers behind websites in conjunction with the participation of the community.

This is an open source project developed in La Salle URL - Human-Environment Research group, Technology Enhanced Learning research line leadered by Daniel Amo-Filva. 

## Dependencies
### Frontend
* [Vue](https://vuejs.org/) - JavaScript framework for building user interfaces
* [Vite](https://vitejs.dev/) - Build tool for modern web development
* [Axios](https://www.npmjs.com/package/axios) - Promise-based HTTP client for the browser and Node.js
* Vue Router - Official router for Vue.js

### Backend
* [Node.js](https://nodejs.org/en/) - JavaScript runtime built on Chrome's V8 JavaScript engine
* [Express](https://www.npmjs.com/package/express) - Fast, unopinionated, minimalist web framework for Node.js
* [Python](https://www.python.org/) - High-level, interpreted programming language
* [MongoDB](https://www.mongodb.com/) - NoSQL database system.

#### Requiere instalation
* [Node.js](https://nodejs.org/en/download/)
* npm: npm is included with Node.js. To install a specific version of npm, you can run npm install -g npm@<version> after installing Node.js.
* [Python](https://www.python.org/downloads/)

#### Optional
* [MongoDB](https://www.mongodb.com/try/download/community)

Choose the appropriate download link for your operating system and follow the installation instructions. Once installed, you can verify the installation by running the appropriate command in your command prompt or terminal:

* Node.js: `node -v` and `npm -v`
* Python: `python --version`
* MongoDB: `mongo --version`

## Installation

### API
On clone use `npm i` to install all the dependencies
Configuration of the API. 

.env file must be placed on ./api/.env
```
PORT = ´API PORT´ :number *requierd
HEADLESS = ´FALSE ON SERVER´ *requierd
USE_MONGO = :boolean *requierd
MONGO_HOST = ´MONGO URL´
DB_NAME = ´MONGO DB NAME´
SITES_COLLECTION = ´MONGO DB COLLECTION NAME´

```
`npm run dev`
Runs the server with the configuration from .env


### FRONT
On clone use npm i to install all the dependencies Configuration of the frontend.

`npm run dev`
Runs the development server using Vite.

`npm run build`
Builds the production-ready files using Vite.

`npm run preview`
Runs a preview of the production build using Vite.

`npm run lint`
Runs the eslint command to check for any errors in .vue, .js, .jsx, .cjs, and .mjs files in the project directory. This command will automatically fix any fixable errors and ignores any files listed in the .gitignore file.

## Team
The project leader for this project is Daniel Amo-Filva, who oversees the development of the project and manages contributions from other developers.

* Dr. Daniel Amo Filvà: [daniel.amo@salle.url.edu](mailto:daniel.amo@salle.url.edu) - [Github](https://github.com/danielamof/)
* Pau Passolas Nadal: [pau.passolas@students.salle.url.edu](mailto:pau.passolas@students.salle.url.edu) - [Github](https://github.com/ppassolas/)
* Dídac Ibars Teixidó: [didac.ibars@students.salle.url.edu](mailto:didac.ibars@students.salle.url.edu) - [Github](https://github.com/TheDidi)

## License
This project is licensed under the MIT. For more information, please refer to the LICENSE file.

