import Vue from "vue";
import Vuex from "vuex";

import { incomes } from "@/store/modules/income.js";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    incomes
  },
});
