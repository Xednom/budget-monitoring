import { apiService } from "@/common/api.service.js";
import {
  FETCH_INCOMES,
  FETCH_TYPE_INCOMES,
  FETCH_AN_INCOME
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_INCOMES,
  SET_AN_INCOME,
} from "@/store/mutations.type";

const state = {
  // a list of state related to expenses

  incomes: [],
  income: {},
  newIncome: {
    wages_and_tips: 0.00,
    interest_income: 0.00,
    dividends: 0.00,
    refunds_reimbursement: 0.00,
    transfer_from_savings: 0.00,
    total_income: 0.00,
    users: null,
    other: []
  },
  loading: false,
  saving: false
};

const getters = {
  // define method to access state value

  expenses: state => {
    return state.incomes;
  },
  expense: state => {
    return state.income;
  },
  loading: state => {
    return state.loading;
  }
};

const mutations = {
  // define mutations to redefine state value

  [FETCH_START](state) {
    state.loading = true;
  },
  [FETCH_END](state) {
    state.loading = false;
  },
  [SET_INCOMES](state, pIncomes) {
    state.incomes = pIncomes;
  },
  [SET_AN_INCOME](state, pIncome) {
    state.income = pIncome;
  }
};

const actions = {
  // define actions like FETCH_AN_EXPENSE

  [FETCH_INCOMES]({ commit }) {
    let endpoint = `/api/v1/income/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_INCOMES, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_AN_INCOME]({ commit }, payload) {
    commit(FETCH_START);
    const income_id = payload;
    let endpoint = `/api/v1/income/${income_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_AN_INCOME, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  }
};

export const expenses = {
  state,
  getters,
  mutations,
  actions
};