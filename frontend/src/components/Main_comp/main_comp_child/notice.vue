<template>
  <div class="notice">
    <div class="title">
      <span class="t_text">通知公示</span>
      <el-divider class="title_divider"></el-divider>
      <div class="n_more">
        <span
          class="n_more_span"
          style="position: relative; text-decoration: none;font-size:14px"
          @click="gotofile()"
          >更多</span
        >
        <i class="el-icon-arrow-right" style="margin-top:2px"></i>
      </div>
    </div>
    <div class="content" v-for="item in notice_list.slice(0, 8)" :key="item.id">
      <el-row class="c_row">
        <el-col :span="6" style="margin-left: 10px"
          ><span style="font-size:14px">{{ item.date }}</span>
        </el-col>
        <el-col :span="16" style="margin-left: 8px; display: flex">
          <el-button
            type="text"
            @click="getPdfUrl(item.id)"
            style="padding: 0px !important; font-size: 16px; color: black;font-size:14px"
            >{{ item.title }}</el-button
          ></el-col
        >
      </el-row>
      <el-divider class="content_divider"></el-divider>
    </div>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      notice_list: [],
      college_id: "",
    };
  },
  mounted() {
    this.getfilelist();
  },
  methods: {
    async getfilelist() {
      const val = JSON.parse(localStorage.getItem("id"));
      if (val < 4) {
        this.college_id = JSON.parse(localStorage.getItem("from_college"));
        const res = await this.$http.get(
          "files/publicity_college/" + this.college_id
        );
        res.data.map((item) => {
          let str = item.title.split(".");
          item.title = str[0];
        });
        this.notice_list = res.data;
      } else if (val == 4) {
        const res = await this.$http.get("files/publicity/");
        this.notice_list = res.data;
      }
    },
    gotofile() {
      this.$router
        .push({
          name: "files",
        })
        .catch(() => {});
    },
    getPdfUrl(id) {
      this.$http({
        method: "get",
        url: "files/publicity/" + id,
        responseType: "blob",
        //设置响应的数据类型为一个包含二进制数据的 Blob 对象
      })
        .then((res) => {
          console.log(res.data.type);
          let blob = new Blob([res.data], { type:"application/pdf;charset=utf-8"}); //就是这里一点差距
          //兼容ie
          if (window.navigator && window.navigator.msSaveBlob) {
            window.navigator.msSaveBlob(blob, filename);
          } else {
            var href = window.URL.createObjectURL(blob); //转成链接让其能供人下载
            window.open(href);
            // downloadElement.href = href; //a标签的href
            // downloadElement.download = filename; //a标签的下载名字
            // document.body.appendChild(downloadElement); //注册这个控件将这个组件加到body尾部
            // downloadElement.click(); //注销掉
            // window.URL.revokeObjectURL(href); //清除生成的链接，会占用一些东西，不知道啥，反正运行慢点
          }
        })
        .catch((e) => {
          console.log("error:" + e);
        });
    },
  },
};
</script>

<style>
.notice {
  background: white;
  width: 100%;
}
.title_divider {
  background: rgb(255, 98, 0);
  width: 80px;
}
.content_divider {
  width: 364px;
}
.title {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  font-weight: bold;
  padding-top: 10px;
  margin-bottom: 20px;
}
.n_more {
  display: flex;
  margin-left: 300px;
  margin-top: -40px;
}

.el-col-18 {
  display: flex;
  justify-content: start;
  align-items: flex-start;
  text-align: start;
}
.n_more_span:before {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  height: 2px;
  width: 100%;
  background: #000;
  transform: scale(0);
  transition: all 0.3s;
}
.n_more_span:hover:before {
  transform: scale(1);
}
</style>