/* eslint-disable no-shadow */
import api from '../api';

const state = {
  help: null,
  token: '',
  list: null,
  loginError: null,
  loading: false,
};

const getters = {
  getHelp(state) { return state.help; },
  getToken(state) { return state.token; },
  getList(state) { return state.list; },
  getLoginError(state) { return state.loginError; },
};

const actions = {
  login({ commit }, data) {
    commit('SET_LOADING', true);
    return api().post('login', data).then((success) => {
      commit('SET_TOKEN', success);
      commit('SET_LOGIN_ERROR', null);
      commit('SET_LOADING', false);
    }).catch((error) => {
      commit('SET_LOGIN_ERROR', error.response.data.error);
      commit('SET_LOADING', false);
    });
    // return api().get('Helps?page=1').then((success) => {
    //   commit('SET_LIST', success.data.data);
    // });
  },
  register({ commit }, data) {
    commit('SET_LOADING', true);
    return api().post('register', data).then((success) => {
      commit('SET_TOKEN', success);
      commit('SET_LOGIN_ERROR', null);
      commit('SET_LOADING', false);
    }).catch((error) => {
      commit('SET_LOGIN_ERROR', error.response.data.error);
      commit('SET_LOADING', false);
    });
  },
};

const mutations = {
  SET_HELP(state, value) {
    state.help = value;
    // console.log('mutations SET_Help', state.data);
  },
  SET_TOKEN(state, value) {
    state.token = value;
  },
  SET_LIST(state, value) {
    state.list = value;
  },
  SET_LOGIN_ERROR(state, value) {
    state.loginError = value;
  },
  SET_LOADING(state, value) {
    state.loading = value;
  },
};


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
