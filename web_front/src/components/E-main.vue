<template xmlns:v-finger="http://www.w3.org/1999/xhtml">
  <div class="E-main"
       v-loading="loading"
       v-finger:swipe="swipe"
       v-finger:press-move="pressMove">
    <div class="album_cls" ref="album_cls">
      <div class="head">
        <img :src="require('../../static/IMG_3570.jpg')" alt="">
      </div>
      <aside class="cls_content">
        <h1>相册分类</h1>
        <el-button type="text" @click="viewOver" style="left: 2rem;position: relative;font-size: 16px;color: white;text-decoration: underline;">查看所有相册</el-button>
        <ul>
          <li v-for="(item, index) in type_pictures" @touchend.stop="aside_current(item)">
            <em>{{ item.title }}</em>
          </li>
        </ul>
      </aside>
    </div>
    <main id="main">
      <div id="models" v-finger:tap.stop="tap"></div>
      <div class="banner">
        <div class="sidebar" :class="focus_sidebar ? 'focus_sidebar ': 'blur_sidebar'" v-finger:tap.stop="unwind"></div>
        <div class="switch" @touchend="switchType">
          <span :style="type === '相册' ? 'left: 0px;' : 'left: 50%;'"></span>
          <em :style="type === '相册' ?  'color: white' : ''">相册</em>
          <em :style="type !== '相册' ?  'color: white' : ''">视频</em>
        </div>
        <div class="search"></div>
      </div>
      <e_content ref="content"></e_content>
      <div class="new">
        <div class="el_new" @click.stop="add_album_video(1)">新建相册</div>
        <div class="el_new" @click.stop="add_album_video(0)">上传</div>
        <div style="position:relative;z-index: 2;width: 100%;height: 100%;" @click.stop="pop"></div>
        <div class="icon">
          <span :style="forward ? 'transform: rotate(0deg)' : 'transform: rotate(180deg)'"></span>
          <span :style="forward ? 'transform: rotate(270deg)' : 'transform: rotate(0deg)'"></span>
        </div>
      </div>
    </main>

    <e_upload v-if="show_upload" ref="upload" @shutdown="closeUpload"></e_upload>
    <e_create v-if="show_create" ref="create" @shutdown="closeCreate"></e_create>
  </div>
</template>

<script>
  import anime from 'animejs'
  import e_content from './E-main_content.vue'
  import e_upload from './base/upload'
  import e_create from './base/create'
  import mojs from 'mo-js'
  import axios from '../router/axios'

export default {
  name: 'E-main',

  components: {e_content, e_upload, e_create, },
  data () {
    return {
      type_pictures: [],
      type: '相册',
      forward: true,
      show_upload: false,
      show_create: false,
      e_anmime: null,
      WIDTH: 180,
      el_cls: null,
      main: null,
      el_new: null,
      models: null,
      focus_sidebar: false,
      loading: true,
    }
  },
  watch: {
    show_upload(val) {
      console.log(val);
    }
  },
  methods: {
    viewOver() {
      this.$refs.content.init();
      this.swipe({direction: 'Left'});
    },
    aside_current(row) {
      this.$refs.content.init(row.id, row.url);
      this.swipe({direction: 'Left'});
    },
    pressMove(e) {

    },
    unwind() {
      this.swipe({direction: 'Right'});
    },
    tap() {
      this.swipe({direction: 'Left'});
    },
    swipe(e) {
      if (!this.el_cls) this.el_cls = document.querySelector('.album_cls');
      if (!this.main) this.main = document.querySelector('main');
      if (!this.el_new) this.el_new = document.querySelector('.new');
      if (!this.models) this.models = document.querySelector('#models');
      if (e.direction === 'Right') {
        this.el_cls.style.left = 0;
        this.main.style.left = `${this.WIDTH}px`;
        this.el_new.style.bottom = `-64px`;
        this.models.style.display = `block`;
        this.focus_sidebar = true;
      }
      if (e.direction === 'Left') {
        this.el_cls.style.left = `-${this.WIDTH}px`;
        this.main.style.left = 0;
        this.el_new.style.bottom = `12px`;
        this.models.style.display = `none`;
        this.focus_sidebar = false;
      }
    },
    async closeCreate() {
      this.show_create = false;
      await this.getAlbums();
    },
    async closeUpload() {
      this.show_upload = false;
      await this.getAlbums();
    },
    add_album_video(type) {
      this.pop(); // 关闭弹窗
      if (!type) {
        this.show_upload = true;
        this.$nextTick(() => {
          this.$refs.upload.open(true);
        })
      } else {
        this.show_create = true;
        this.$nextTick(() => {
          this.$refs.create.open(true);
        })
      }
    },
    pop() {
      document.querySelector('.new').style.transform = 'scale(1.1)';
      setTimeout(() => {
        document.querySelector('.new').style.transform = 'scale(1)';
      }, 300);
      if (this.e_anmime) this.e_anmime.pause();
      var value = 0;
      this.forward ? value = -80 : value = 0;
      this.e_anmime = anime({
        targets: '.el_new',
        translateY: value,
        translateX: (el, i)=>{if (!this.forward) {return 0;}return (i+1) % 2 === 0 ? 60 : -60},
        direction: 'alternate',
        delay: (el, i, l) => {return i * 200},
        autoplay: true,
        loop: false,
        opacity: this.forward ? 1 : 0,
        rotate: this.forward ? '1turn' : '2turn'
      });
      this.forward ? this.forward = false : this.forward = true;
    },
    switchType() {
        this.type === '相册' ? this.type = '视频' : this.type = '相册'
    },
    getAlbums(album_id) {
      let params = {};
      album_id
        ?
          (params['album_id'] = album_id)
        :
          (params['type'] = 'all');
      this.loading = true;
      axios.post('/api/get_album/', params, (e) => {
        this.type_pictures = e.data;
        this.loading = false;
      });
    }
  },

  mounted: function () {
    const burst = new mojs.Burst({
      radius:   { 0: 100 },
      count:    10,
      children: {
        shape:      'polygon',
        points:     7,
        fill:       { 'cyan' : 'yellow' },
        duration:   1000,
        delay:      'stagger(20, rand(0, 25))'
      }
    });
    this.getAlbums();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.E-main {
  height: 100%;
  main {
    position: relative;
    left: 0;
    height: 100%;
    transition: all 0.4s;
  }
  #models {
    display: none;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: #333;
    opacity: 0.4;
    z-index: 1000;
    transition: all 0.4s;
  }
  .album_cls {
    position: fixed;
    left: -180px;
    top: 0;
    width: 180px;
    height: 100%;
    color: white;
    background-color: #f2465b;
    transition: all 0.4s;
    z-index: 999;
    .cls_content {
      h1 {
        width: calc(100% - 44px);
        font-weight: normal;
        padding: 0 12px 2px;
        margin: 12px auto;
        border-bottom: 1px solid #ffeded;
      }
      ul {
        width: calc(100% - 12px);
        padding: 0 6px;
        li {
          height: 34px;
          line-height: 34px;
          padding-left: 24px;
          text-decoration: underline;
          em {
            font-style: normal;
          }
        }
      }
    }
    .head {
      display: flex;
      align-items: center;
      justify-content: space-around;
      padding: 24px;
      img {
        width: 64px;
        border-radius: 50%;
      }
    }
  }
  .banner {
    position: relative;
    left: 0;
    background: url("../assets/banner_bg.jpg") repeat-x left top;
    background-size: 100% 88px;
    width: 100%;
    height: 58px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.4s;
    .focus_sidebar {
      background-image: url("../assets/sidebar_focus.png");
      background-size: 24px 24px;
    }
    .blur_sidebar {
      background-image: url("../assets/sidebar.png");
      background-size: 24px 24px;
    }
    .sidebar {
      display: inline-block;
      background-repeat: no-repeat;
      background-position: center;
      width: 40px;
      height: 30px;
      padding-left: 64px;
    }
    .switch {
      position: relative;
      width: 120px;
      height: 30px;
      background-color: white;
      border-radius: 12px;
      .left {
        float: left;
      }
      .right {
        float: right;
      }
      em {
        position: relative;
        display: inline-block;
        float: left;
        height: 100%;
        width: 50%;
        line-height: 30px;
        text-align: center;
        letter-spacing: 2px;
        font-style: normal;
        transition: color 0.3s;
        color: darksalmon;
      }
      span {
        position: absolute;
        transition: all 0.3s ease;
        display: inline-block;
        height: 100%;
        width: 50%;
        border-radius: 12px;
        background-color: #fca8b2;
        color: white;

      }
    }
    .search {
      background: url("../assets/search.png") no-repeat center;
      background-size: 24px 24px;
      width: 40px;
      height: 30px;
      padding-right: 64px;
    }
  }
  .new {
    position: fixed;
    bottom: 12px;
    left: 50%;
    width: 64px;
    height: 64px;
    margin-left: -32px;
    border-radius: 50%;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: space-around;
    box-shadow: 0 2px 0 0 rgba(250, 208, 196, 0.63), 0 0 0 0.5px rgba(255, 210, 253, 0.56);
    transition: all 0.3s;
    .el_new {
      position: absolute;
      opacity: 0;
      width: 64px;
      height: 64px;
      border-radius: 50%;
      text-align: center;
      line-height: 64px;
      color: white;
      background-color: #fad0c4;
      border: 1px solid #c59c90;
    }
    .icon {
      position: absolute;
      display: inline-block;
      left: 0;
      top: 0;
      right: 0;
      bottom: 0;
      margin: auto;
      width: 46%;
      height: 46%;
      span {
        display: block;
        position: absolute;
        left: 0;
        top: 50%;
        width: 100%;
        height: 4px;
        margin-top: -2px;
        border-radius: 1px;
        background-color: rgb(251,167,172);
        transition: all 0.3s;
      }
      span:last-child {
        transform: rotate(90deg);
      }
    }
  }
}
</style>
