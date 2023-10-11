<template>
  <div class="files">
    <Register_title> </Register_title>
    <div class="bar">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/Main' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>通知公示</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="divider">
      <el-divider class="bar_divider"></el-divider>
    </div>
    <div class="n_list" v-for="item in notice_list" :key="item.id">
      <el-row class="c_row">
        <el-col
          style="display: flex; justify-content: start; align-items: center;margin-left:300px;margin-top:10px"
        >
          <el-button
            type="text"
            @click="getPdfUrl(item.id)"
            style="padding: 0px !important; font-size: 16px; color: black"
            >{{ item.title }}</el-button
          ></el-col
        >
      </el-row>
      <el-col
        style="display: flex; justify-content: center; align-items: center;margin-top:10px"
        ><span>{{ item.date }}</span>
      </el-col>
    </div>
    <!-- <div class="page">
      <span class="pre" @click="prePage">&lt;&nbsp;上一页</span>
      <template v-for="(item, index) in page">
        <span
          :class="{ num: true, choosed: offset == item }"
          :key="index"
          @click="toPage(item)"
          >{{ item }}</span
        >
      </template>
      <span class="next" @click="nextPage">下一页&nbsp;&gt;</span>
    </div> -->
  </div>
</template>

<script>
import pdf from "vue-pdf/src/vuePdfNoSssNoWorker";
import Register_title from "@/components/Register_title.vue";
export default {
  props: {},
  components: {
    pdf,
    Register_title,
  },
  data() {
    return {
      id: "",
      files: "",
      pdfUrl: "",
      flag: 0,
      numPages: undefined,
      temp: {},
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
        this.total=res.data.length;
        console.log(this.total);
        this.notice_list = res.data;
      } else if (val == 4) {
        const res = await this.$http.get("files/publicity/");
        this.notice_list = res.data;
      }
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
          let blob = new Blob([res.data], {
            type: "application/pdf;charset=utf-8",
          }); //就是这里一点差距
          //兼容ie
          if (window.navigator && window.navigator.msSaveBlob) {
            window.navigator.msSaveBlob(blob, filename);
          } else {
            var href = window.URL.createObjectURL(blob); //转成链接让其能供人下载
            window.open(href);
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
.files {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
.n_list {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.c_row {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.bar {
  margin-top: 15px;
  margin-left: 250px;
}
.divider {
  width: 100%;
  height: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.bar_divider {
  width: 70%;
}
</style>