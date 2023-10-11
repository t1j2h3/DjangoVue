<template>
  <div class="g3">
    <el-upload
      class="upload-demo"
      action=""
      :before-upload="beforeUpload"
      :on-success="handlesuccess"
      :http-request="modeUpload"
      ref="upload"
      style="display: flex"
      :show-file-list="false"
    >
      <el-button size="small" type="primary">选择文件</el-button>
      <div slot="tip" class="el-upload__tip" style="margin-left: 20px">
        只能上传pdf文件。
      </div>
    </el-upload>
    <el-table
      :data="uploadFilesList"
      style="width: 100%; margin-top: 20px"
      border
    >
      <el-table-column prop="college_title" label="所属院" width="240">
        <template slot-scope="scope">
          {{ scope.row.college_title }}
        </template>
      </el-table-column>
      <el-table-column prop="title" label="文件名" width="432">
        <template slot-scope="scope">
          {{ scope.row.title }}
        </template>
      </el-table-column>
      <el-table-column width="120" prop="date" label="上传日期" />
      <el-table-column
        prop="function"
        width="180"
        :show-overflow-tooltip="true"
        label="功能"
      >
        <template slot-scope="scope">
          <el-button
            type="primary"
            size="mini"
            @click="delete_file(scope.row.id)"
            >删除</el-button
          >
          <el-button
            type="primary"
            size="mini"
            @click="down_file(scope.row.title, scope.row.id)"
            >下载</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      uploadFilesList: [],
      fileList: [],
      mode: "",
      file_name: "",
      college_id: "",
    };
  },
  mounted() {
    this.getfilelist();
  },
  methods: {
    async getfilelist() {
      const val = JSON.parse(localStorage.getItem("id"));
      if (val == 3) {
        this.college_id = JSON.parse(localStorage.getItem("from_college"));
        const res = await this.$http.get(
          "files/publicity_college/" + this.college_id
        );
        console.log(res)
        this.uploadFilesList = res.data;
      } else if (val == 4) {
        const res = await this.$http.get("files/publicity/");
        this.uploadFilesList = res.data;
      }
    },
    async modeUpload(item) {
      const val2 = JSON.parse(localStorage.getItem("from_college"));
      this.mode = item.file;
      let fd = new FormData();
      let year = new Date().getFullYear();
      //月份是从0月开始获取的，所以要+1;
      let month = new Date().getMonth() + 1;
      //日
      let day = new Date().getDate();
      let time = year + "-" + month + "-" + day;
      fd.append("file_obj", this.mode);
      fd.append("title", this.mode.name);
      fd.append("college", val2);
      fd.append("date", time);
      // console.log(fd);
      const res = await this.$http.post("files/publicity/", fd);
      console.log(res)
      if (res.status == 200) {
        this.$message({
          type: "success",
          message: "上传成功!",
        });
        this.getfilelist();
      } else {
        this.$message({
          type: "error",
          message: response.data.entail,
        });
      }
    },
    beforeUpload(file) {
      console.log(file);
      if (
        file.type == "application/pdf"
      ) {
        return true;
      } else {
        this.$message({
          message: "请重新点击选择文件传入符合标准的文件",
          type: "warning",
        });
        return false;
      }
    },
    handlesuccess(response, file, fileList) {
      // console.log(response, file, fileList);
      // console.log("success");
    },
    async delete_file(id) {
      const res = await this.$http.delete("files/publicity/" + id);
      console.log(res);
      if (res.status == 200) {
        this.$message({
          message: "删除成功",
          type: "success",
        });
        this.getfilelist();
      } else {
        this.$message({
          message: "删除失败",
          type: "error",
        });
      }
    },

    async down_file(title, id) {
      var filename = title;
      this.$http
        .get("files/publicity/" + id, {
          params: this.filter,
          responseType: "blob",
        }) //这里的传递要加responseType:'blob'指定类型，后端不需要处理这个类型，只需要传过去就行
        .then((res) => {
          let blob = new Blob([res.data], { type: res.data.type }); //就是这里一点差距
          //兼容ie
          if (window.navigator && window.navigator.msSaveBlob) {
            window.navigator.msSaveBlob(blob, filename);
          } else {
            var downloadElement = document.createElement("a"); //模拟一个a标签与asp.net试图操作类似
            var href = window.URL.createObjectURL(blob); //转成链接让其能供人下载
            downloadElement.href = href; //a标签的href
            downloadElement.download = filename; //a标签的下载名字
            document.body.appendChild(downloadElement); //注册这个控件将这个组件加到body尾部
            downloadElement.click(); //注销掉
            window.URL.revokeObjectURL(href); //清除生成的链接，会占用一些东西，不知道啥，反正运行慢点
          }
          console.log(res);
        });
    },
  },
};
</script>

<style>
.fileupload {
  width: 100%;
  display: flex;
  justify-content: start;
}
</style>