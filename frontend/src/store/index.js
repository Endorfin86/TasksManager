import { createStore } from 'vuex'

const store = createStore({
  state () {
    return {
    token: localStorage.getItem('token')
    }
  },
  mutations: {
    TOKEN_CHANGE(state, token) {
      state.token = token
  }
  },
  actions: {
    TOKEN_ACTION(context, token) {
      context.commit('TOKEN_CHANGE', token)
  }
  },
  getters: {
    TOKEN_GETTER(state) {
      return state.token
    }
  }
})

export default store