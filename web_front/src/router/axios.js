import axios from 'axios'

function axios_get(url, params, callback) {
  axios.get(url, {params: params})
    .then((response) => {
      if (callback) {
        callback(response.data)
      }
    }).catch((error) => {
      console.log(error);
    })
}

function axios_post(url, params, callback) {
  axios.post(url, params, {
    /*headers: {
      'X-CSRFToken': 'xxxxxx',
      "Content-Type": 'application/json'
    }*/
  }).then((response) => {
    if (callback) {
      callback(response.data)
    }
  }).catch((error) => {
    console.log(error);
  })
}

export default {
  post: axios_post,
  get: axios_get
}
