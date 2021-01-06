import request from '@/utils/request'
const api_group='telnet'

export default{

   makevlan(pojo) {
    return request({
      url: `/${api_group}/vlan`,
      method: 'post',
      data: pojo
    })
  },
   vlan(token) {
    return request({
      url: `/${api_group}/vlan`,
      method: 'get',
    })
  }
  ,trunk() {
    return request({
      url: `/${api_group}/trunk`,
      method: 'post'
    })
  }

  ,divide(pojo) {
      return request({
        url: `/${api_group}/divide`,
        method: 'put',
        data: pojo
      })
    }
    ,ping(token) {
      return request({
        url: `/${api_group}/ping`,
        method: 'get',
      })
    }
    ,iproute() {
      return request({
        url: `/${api_group}/iproute`,
        method: 'get'
      })
    }


}
