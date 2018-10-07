<template>
  <div class="E-main_content">
    <div>
      <ul>
        <li v-for="(item, index) in data" :key="item.id">
          <el-card :body-style="{ padding: '0px' }">
            <img :src="item.src" :alt="item.des" class="image">
            <div style="padding: 14px;">
              <span>{{ item.des }}</span>
              <div class="bottom clearfix">
                <time class="time">{{ item.date }}</time>
              </div>
            </div>
          </el-card>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'E-main_content',
  data () {
    return {
        data: [{
          des: '北海一日游', // 描述
          src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOATA8mjLxD0MqvjhfgeAqVbnsOodlHgTP0OaNEzMFsBGBVxZT', // 地址
          date: '2018-8-9', // 拍摄时间
          relevant: ['何沁','黄文章'], // 照片有谁
          group: ['旅游','恋爱'], // 分类
          point: '广西北海', // 地点
          type: 'picture' // 视频还是图片
        },{
          des: '桂林一日游', // 描述
          src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyk6zOHyWwjpMXoStdzXX_NgtmAArzU9IvdsujQ4kOKZiA1FCC', // 地址
          date: '2018-8-9', // 拍摄时间
          relevant: ['何沁','黄文章'], // 照片有谁
          group: ['旅游','恋爱'], // 分类
          point: '广西桂林', // 地点
          type: 'picture' // 视频还是图片
        }]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.E-main_content {
  width: 70%;
  margin: 0 auto;
  margin-top: -64px;
  li {
    position: relative;
    list-style-type: none;
    margin-top: 24px;
    img {
      width: 100%;
    }
    summary {
      position: absolute;
      bottom: 0;
      left: 0;
      width: calc(100% - 8px);
      height: 36px;
      line-height: 36px;
      color: white;
      text-align: left;
      padding: 4px;
      background: linear-gradient(90deg, #00000094, #ffffff8c);
    }
  }
}
</style>
