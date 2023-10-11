<template>
  <div class="a">
    <el-form
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      label-width="140px"
      class="demo-ruleForm"
    >
      <el-form-item
        label="上传成绩单"
        prop="apply_letter"
        style="width: 400px"
        size="medium"
      >
        <el-upload
          class="upload-demo"
          action=""
          :before-upload="beforeupload"
          :on-success="handlesuccess"
          :http-request="modeUpload"
          :on-error="handleError"
          :auto-upload="false"
          ref="upload"
        >
          <el-button size="small" type="primary">选择文件</el-button>
          <div slot="tip" class="el-upload__tip">
            只能上传pdf文件，且不超过100kb。
          </div>
        </el-upload>
        <el-button
          size="small"
          type="primary"
          @click="downUpload()"
          v-show="this.file_name!= null ? true : false"
          >下载文件</el-button
        >
      <div>
        <span v-show="this.file_name!= null ? true : false">{{this.file_name}}</span>
      </div>
      </el-form-item>
      <el-form-item class="a_btn">
        <el-button @click="saveForm('ruleForm')">保存</el-button>
        <el-button type="primary" @click="submitForm('ruleForm')"
          >提交</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      filedata: {},
      temp: "",
      ruleForm: {
        First_application: "",
        semester: "",
        apply_letter: "",
        talking_date: "",
        talker: "",
      },
      fileList: [],
      rules: {},
      mode: "",
      file_name:'',
    };
  },
  created() {
    this.showmessage();
  },
  methods: {
    async showmessage() {
      this.temp = JSON.parse(localStorage.getItem("account"));
      // console.log(this.temp);
      const res = await this.$http.get("/user/get2/" + this.temp);
      // console.log(res);
      this.ruleForm.First_application = res.data.First_application;
      this.ruleForm.semester = res.data.semester;
      this.file_name = res.data.apply_letter;
      this.ruleForm.talking_date = res.data.talking_date;
      this.ruleForm.talker = res.data.talker;
    },
    modeUpload(item) {
      this.mode = item.file;
    },
    handleError(err, file, fileList) {
      // console.log(err,file,fileList)
    },

    handlesuccess(response, file, fileList) {
      // console.log(response, file, fileList);
      // console.log("success");
    },
    saveForm(ruleForm) {
      this.$refs[ruleForm].validate((valid) => {
        if (valid) {
          localStorage.setItem("a_information", JSON.stringify(this.ruleForm));
          this.$message({
            message: "保存成功",
            type: "success",
          });
        } else {
          this.$message.error("保全信息不完整，请继续填写完整");
          return false;
        }
      });
    },
    downUpload() {
      var filename = "入党申请书.pdf";
      this.$http
        .get("files/apply_letter/" + this.temp, {
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
    submitForm(ruleForm) {
      this.$refs[ruleForm].validate(async (valid) => {
        if (valid) {
          this.$refs.upload.submit();
          let fd = new FormData();
          fd.append("apply_letter", this.mode);
          fd.append("First_application", this.ruleForm.First_application);
          fd.append("semester", this.ruleForm.semester);
          fd.append("talking_date", this.ruleForm.talking_date);
          fd.append("talker", this.ruleForm.talker);
          // console.log(fd);
          // console.log(this.ruleForm)
          const res = await this.$http.put("user/put2/" + this.temp, fd);
          console.log(res);
          if (res.status == 200) {
            this.$message({
              message: "提交成功",
              type: "success",
            });
          } else {
            this.$message.error("提交失败");
          }
        } else {
          this.$message.error("保全信息不完整，请继续填写完整");
          return false;
        }
      });
    },
    handleRemove(file, fileList) {
      // console.log(file, fileList);
    },
    handleExceed(files, fileList) {
      this.$message.warning(
        `当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${
          files.length + fileList.length
        } 个文件`
      );
    },
    handlesuccess(response, file, fileList) {
    },
    beforeupload(file) {
      if (file.type != "application/pdf") {
        this.$message({
          message: "请重新点击选择文件传入符合标准的文件",
          type: "warning",
        });
        return false;
      } else return true;
    },
  },
};
</script>

<style>
.a {
  width: 100%;
  height: 100%;
  background: #fff;
}
.demo-ruleForm {
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.a_btn {
  margin-left: -140px;
}
</style>
