import request from '@/utils/request'
const api_group='telnet'
export default{
    makevlan(device){
        return request({
            url:`/${api_group}/vlan`,
            method:'post',
            data:device
        })
    },
    vlan(){
        return request({
            url:`/${api_group}/vlan`,
            method:'get',
        })
    },
    trunk(){
        return request({
            url:`/${api_group}/trunk`,
            method:'post',
        })
    },
    divide(device){
      return request({
          url:`/${api_group}/divide`,
          method:'put',
          data:device
      })
     },
     ping(){
         return request({
             url:`/${api_group}/ping`,
             method:'get',
         })
     },
     iproute(){
         return request({
             url:`/${api_group}/iproute`,
             method:'get',
         })
     },
}