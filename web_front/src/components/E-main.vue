<template>
  <div class="E-main">
    <div class="banner">
      <div class="sidebar"></div>
      <div class="switch" @touchend="switchType">
        <span :style="type === '相册' ? 'left: 0px;' : 'left: 50%;'"></span>
        <em :style="type === '相册' ?  'color: white' : ''">相册</em>
        <em :style="type !== '相册' ?  'color: white' : ''">视频</em>
      </div>
      <div class="search"></div>
    </div>
    <e_content></e_content>
    <div class="new">
      <div class="el_new" @click.stop="add_album_video(0)">新建相册</div>
      <div class="el_new" @click.stop="add_album_video(1)">上传</div>
      <div style="position:relative;z-index: 2;width: 100%;height: 100%;" @click.stop="pop"></div>
      <div class="icon">
        <span :style="forward ? 'transform: rotate(0deg)' : 'transform: rotate(180deg)'"></span>
        <span :style="forward ? 'transform: rotate(270deg)' : 'transform: rotate(0deg)'"></span>
      </div>
    </div>

    <e_upload v-if="show_upload" ref="upload" @shutdown="closeUpload"></e_upload>
  </div>
</template>

<script>
  import anime from 'animejs'
  import e_content from './E-main_content.vue'
  import e_upload from './base/upload'

export default {
  name: 'E-main',

  components: {e_content, e_upload, },
  data () {
    return {
      type: '相册',
      forward: true,
      show_upload: false,
      e_anmime: null
    }
  },
  watch: {
    show_upload(val) {
      console.log(val);
    }
  },
  methods: {
    closeUpload() {
      this.show_upload = false;
    },
    add_album_video(type) {
      this.pop(); // 关闭弹窗
      if (!type) {
        this.show_upload = true;
        this.$nextTick(() => {
          this.$refs.upload.open(true);
        })
      } else {
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
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.E-main {
  height: 100%;
  .banner {
    background: url("../assets/banner_bg.jpg") repeat-x left top;
    background-size: 100% 88px;
    width: 100%;
    height: 58px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    .sidebar {
      display: inline-block;
      background: url("../assets/sidebar.png") no-repeat center;
      background-size: 24px 24px;
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
