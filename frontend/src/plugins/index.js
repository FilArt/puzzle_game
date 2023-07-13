/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import router from "../router";
import pinia from "../store";
import api from "./axios";
import vuetify from "./vuetify";
import { loadFonts } from "./webfontloader";

export function registerPlugins(app) {
  loadFonts();
  app.use(vuetify).use(pinia).use(router).use(api);
}
