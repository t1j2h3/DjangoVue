<template>
  <div>
    <el-menu
      :default-active="selectedMenu"
      mode="horizontal"
      @select="handleMenuSelect"
    >
      <el-menu-item index="courses_for_activists">荣誉表彰</el-menu-item>
      <el-menu-item index="courses_for_leaders">论文创新项目</el-menu-item>
      <el-menu-item index="courses_for_entrepreneurs">学科竞赛各类竞赛</el-menu-item>
      <el-menu-item index="courses_for_b1">实践活动</el-menu-item>
      <el-menu-item index="courses_for_b2">文体竞赛公益活动</el-menu-item>
      <el-menu-item index="courses_for_b3">学生干部经历</el-menu-item>
      <el-menu-item index="courses_for_b4">日常扣分</el-menu-item>
    </el-menu>
    <div v-if="selectedMenu === 'courses_for_activists'">
      <h3 style="font-weight: bold;">最高分：15分</h3>
      <img src="@/assets/b1.jpg" alt="荣誉表彰" style="max-width: 100%; height: auto;">
      <h3>自评分</h3>
      <el-input v-model="ruleForm.courses_for_activists.selfScore"></el-input>
      <h3>详细说明</h3>
      <el-input v-model="ruleForm.courses_for_activists.details" type="textarea" autosize></el-input>
      <h3>上传相关文件</h3>
      <el-upload
        class="upload-demo"
        action="/upload"
        :before-upload="beforeUpload"
        :on-success="handleSuccess"
        :http-request="modeUpload"
        :on="handleError"
        :auto-upload="false"
        ref="upload"
      >
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">
          文件大小不能超过500kb
        </div>
      </el-upload>
    </div>
    <div v-if="selectedMenu === 'courses_for_leaders'">
      <h3 style="font-weight: bold;">最高分：20分</h3>
      <img src="@/assets/b2.jpg" alt="论文创新项目" style="max-width: 100%; height: auto;">
      <h3>自评分</h3>
      <el-input v-model="ruleForm.courses_for_activists.selfScore"></el-input>
      <h3>详细说明</h3>
      <el-input v-model="ruleForm.courses_for_activists.details" type="textarea" autosize></el-input>
      <h3>上传相关文件</h3>
      <el-upload
        class="upload-demo"
        action="/upload"
        :before-upload="beforeUpload"
        :on-success="handleSuccess"
        :http-request="modeUpload"
        :on="handleError"
        :auto-upload="false"
        ref="upload"
      >
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">
          文件大小不能超过500kb
        </div>
      </el-upload>
    </div>
    <div v-if="selectedMenu === 'courses_for_entrepreneurs'">
      <h3 style="font-weight: bold;">最高分：30分</h3>
      <img src="@/assets/b3.jpg" alt="学科竞赛" style="max-width: 100%; height: auto;">
      <h3>自评分</h3>
      <el-input v-model="ruleForm.courses_for_activists.selfScore"></el-input>
      <h3>详细说明</h3>
      <el-input v-model="ruleForm.courses_for_activists.details" type="textarea" autosize></el-input>
      <h3>上传相关文件</h3>
      <el-upload
        class="upload-demo"
        action="/upload"
        :before-upload="beforeUpload"
        :on-success="handleSuccess"
        :http-request="modeUpload"
        :on="handleError"
        :auto-upload="false"
        ref="upload"
      >
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">
          文件大小不能超过500kb
        </div>
      </el-upload>
    </div>
    <div v-if="selectedMenu === 'courses_for_b1'">
      <h3 style="font-weight: bold;">最高分：5分</h3>
      <img src="@/assets/b4.jpg" alt="实践活动" style="max-width: 100%; height: auto;">
      <h3>自评分</h3>
      <el-input v-model="ruleForm.courses_for_activists.selfScore"></el-input>
      <h3>详细说明</h3>
      <el-input v-model="ruleForm.courses_for_activists.details" type="textarea" autosize></el-input>
      <h3>上传相关文件</h3>
      <el-upload
        class="upload-demo"
        action="/upload"
        :before-upload="beforeUpload"
        :on-success="handleSuccess"
        :http-request="modeUpload"
        :on="handleError"
        :auto-upload="false"
        ref="upload"
      >
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">
          文件大小不能超过500kb
        </div>
      </el-upload>
    </div>
    <div v-if="selectedMenu === 'courses_for_b2'">
      <h3 style="font-weight: bold;">最高分：10分</h3>
      <img src="@/assets/b5.jpg" alt="文体竞赛" style="max-width: 100%; height: auto;">
      <h3>自评分</h3>
      <el-input v-model="ruleForm.courses_for_activists.selfScore"></el-input>
      <h3>详细说明</h3>
      <el-input v-model="ruleForm.courses_for_activists.details" type="textarea" autosize></el-input>
      <h3>上传相关文件</h3>
      <el-upload
        class="upload-demo"
        action="/upload"
        :before-upload="beforeUpload"
        :on-success="handleSuccess"
        :http-request="modeUpload"
        :on="handleError"
        :auto-upload="false"
        ref="upload"
      >
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">
          文件大小不能超过500kb
        </div>
      </el-upload>
    </div>
    <div v-if="selectedMenu === 'courses_for_b3'">
      <h3 style="font-weight: bold;">最高分：20分</h3>
      <img src="@/assets/b6.jpg" alt="学生干部" style="max-width: 100%; height: auto;">
      <h3>自评分</h3>
      <el-input v-model="ruleForm.courses_for_activists.selfScore"></el-input>
      <h3>详细说明</h3>
      <el-input v-model="ruleForm.courses_for_activists.details" type="textarea" autosize></el-input>
      <h3>上传相关文件</h3>
      <el-upload
        class="upload-demo"
        action="/upload"
        :before-upload="beforeUpload"
        :on-success="handleSuccess"
        :http-request="modeUpload"
        :on="handleError"
        :auto-upload="false"
        ref="upload"
      >
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">
          文件大小不能超过500kb
        </div>
      </el-upload>
    </div>
    <div v-if="selectedMenu === 'courses_for_b4'">
      <h3 style="font-weight: bold;">累计扣分</h3>
      <img src="@/assets/b7.jpg" alt="日常扣分" style="max-width: 100%; height: auto;">
      <h3>自评分</h3>
      <el-input v-model="ruleForm.courses_for_activists.selfScore"></el-input>
      <h3>详细说明</h3>
      <el-input v-model="ruleForm.courses_for_activists.details" type="textarea" autosize></el-input>
      <h3>上传相关文件</h3>
      <el-upload
        class="upload-demo"
        action="/upload"
        :before-upload="beforeUpload"
        :on-success="handleSuccess"
        :http-request="modeUpload"
        :on="handleError"
        :auto-upload="false"
        ref="upload"
      >
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">
          文件大小不能超过500kb
        </div>
      </el-upload>
    </div>
    <!--    <div style="display: flex; justify-content: center; height: 100vh;">-->
    <!--      <div>-->
    <!--        <el-button size="small" type="primary">保存</el-button>-->
    <!--        <el-button size="small" type="primary">提交</el-button>-->
    <!--      </div>-->
    <!--    </div>-->
    <div style="display: flex; justify-content: center;">
      <el-button @click="saveForm('ruleForm')">保存</el-button>
      <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedMenu: 'courses_for_activists',
      ruleForm: {
        courses_for_activists: {
          highestScore: '',
          selfScore: '',
          details: ''
        },
        courses_for_leaders: {
          highestScore: '',
          selfScore: '',
          details: ''
        },
        courses_for_entrepreneurs: {
          highestScore: '',
          selfScore: '',
          details: ''
        }
      }
    };
  },
  methods: {
    handleMenuSelect(menu) {
      this.selectedMenu = menu;
    },
    beforeUpload(file) {
      const isPDF = file.type === 'application/pdf';
      const isLt500K = file.size / 1024 < 500;
      if (!isPDF) {
        this.$message('只能上传pdf文件');
      }
      if (!isLt500K) {
        this.$message('文件大小不能超过500kb');
      }
      return isPDF && isLt500K;
    },
    saveForm(ruleForm) {
      this.$refs[ruleForm].validate((valid) => {
        if (valid) {
          localStorage.setItem("d_information", JSON.stringify(this.ruleForm));
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
    submitForm(ruleForm) {
      this.$refs[ruleForm].validate(async (valid) => {
        if (valid) {
          this.$refs.upload.submit();
          let fd = new FormData();
          fd.append("voluntary_letter", this.mode);
          fd.append("number", this.ruleForm.number);
          fd.append("mass_discussion", this.ruleForm.mass_discussion);
          fd.append("probation_date", this.ruleForm.probation_date);
          const res = await this.$http.put("user/put5/" + this.temp, fd);
          console.log(res)
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
    handleSuccess(response, file, fileList) {
      this.$message.success('文件上传成功');
    },
    modeUpload() {
      // 自定义上传方法
    },
    handleError() {
      this.$message('文件上传失败');
    }
  }
};
</script>

