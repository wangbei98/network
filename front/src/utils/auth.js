import Cookies from 'js-cookie'

const TokenKey = 'User-Token'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

export function setUser(token,id,phone,permissions) {
  Cookies.set("User-Token", token)
  Cookies.set("User-Id", id)
  Cookies.set("User-Name", phone)
  Cookies.set("User-Permissions", permissions)
}

export function getUser() {
  return {
    token:Cookies.get("User-Token"),
    id:Cookies.get("User-Id"),
    name:Cookies.get("User-Name"),
    permissions:Cookies.get("User-Permissions")
  }
}

export function removeUser() {
  Cookies.remove("User-Token")
  Cookies.remove("User-Id")
  Cookies.remove("User-Name")
  Cookies.remove("User-Permissions")
}
