<template>
  <div class="E-main_content" v-loading="loading">
    <div class="content">
      <ul>
        <li v-for="(item, index) in data" :key="index" @click="frontAlbum(index)">
          <el-card class="box-card">
            <img v-if="item.url" :src="item.url" :alt="item.name">
            <el-card class="box-card" v-if="!item.url">
              <div v-if="!item.url" class="normal">相册里还没有照片哦,赶快来上传第一张吧!</div>
            </el-card>
            <div>
              <h4>{{ item.title }}<span v-if="item.count">里面有&nbsp;{{ item.count }}&nbsp;张图片</span><span v-if="item.size">大小：{{ Math.floor(item.size / 1024) }} KB</span></h4>
              <p class="car"><span>{{ item.point }}</span><span>{{ item.createTime }}</span></p>
            </div>
          </el-card>
        </li>
        <el-card class="box-card" v-if="data.length === 0">
          <div class="normal">相册里还没有照片哦,赶快来上传第一张吧!</div>
        </el-card>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from '../router/axios'
import bus from '../router/bus'

export default {
  name: 'E-main_content',
  data () {
    return {
      data: [],
      el: null,
      loading: true
    }
  },
  props: {
    title: {type: String, default: '获取标题失败'}
  },

  methods: {
    frontAlbum(index) {
      this.init(this.data[index].id, this.data[index].url)
    },
    init(id, url) {
      var vm = this;
      var temp = {};
      if (id) {
        temp['album_id'] = id;
      } else {
        temp['type'] = 'all';
      }
      this.loading = true;
      axios.post('/api/get_album/', temp, (e) => {
        vm.data = e.data;
        this.loading = false;
      });
    },
    update() {
      this.init();
    }
  },

  mounted: function () {
    this.init();
    bus.$on('update', this.update);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.E-main_content {
  position: relative;
  padding: 0 12px;
  height: calc(100% - 58px);
  width: calc(100% - 24px);
  overflow: auto;
  margin: 0 auto;
  left: 0;
  transition: all 0.4s;
  .content {
    padding-bottom: 12px;
    ul {
      padding-top: 12px;
      li:first-child {
        margin: 0;
      }
      li {
        width: 100%;
        margin: 0 auto;
        list-style-type: none;
        overflow: hidden;
        margin-top: 12px;
        padding-bottom: 12px;
        .normal {
          font-size: 13px;
          padding: 4px;
        }
        div {
          h4 {
            font-size: 16px;
            margin: 4px 0;
            color: #606266;
            span {
              float: right;
              font-size: 14px;
              color: #7f7f7f;
              font-weight: normal;
            }
          }
          p {
            display: flex;
            align-items: center;
            justify-content: space-between;
          }
        }
        .car {
          span {
            color: #7f7f7f;
          }
          span:first-child {
            background: url("../assets/point_icon.png") no-repeat left center;
            background-size: 12px 16px;
            text-indent: 18px;
          }
          span:last-child {
          }
        }
        img {
          width: 100%;
          border-radius: 8px;
        }
      }
    }
  }
}
</style>
