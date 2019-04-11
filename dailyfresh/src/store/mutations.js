import axios from 'axios'
export const setLoginStatus = (state) => {
  let current = Bmob.User.current()
  if (current) {
    state.isLogin = true
    state.username = current.username
    state.userId = current.objectId
    axios.post('/getCartCount', {'userId': current.objectId}).then(res => {
      state.cartCount = res.data.count
    })
  } else {
    state.isLogin = false
    state.username = null
  }
};

export const setUserInfo = (state, addressee, address, phone) => {
  state.userAddressee = addressee
  state.userAddress = address
  state.userPhone = phone
}

export const setAdmin = (state, data) => {
  state.adminId = data
}

export const addCartCount = (state) => {
  state.cartCount++
}

export const setNewLogin = (state, data) => {
  state.newLogin = data
}
