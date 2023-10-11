<template>
  <div class="f">
    <el-row :gutter="20">
      <el-col :span="4">
        <el-button type="primary" @click="dialogFormVisible = true"
          >申请关系转接</el-button
        ></el-col
      >
      <el-col :span="4"> <a_downdialog></a_downdialog></el-col>
    </el-row>
    <el-dialog
      title="申请关系转接"
      :visible.sync="dialogFormVisible"
      center
      :append-to-body="true"
      class="el_dialog"
    >
      <el-form
        ref="form1"
        :model="form"
        label-width="100px"
        :rules="rules"
        :validate-on-rule-change="false"
        class="f_form"
      >
        <el-form-item label="原学院" prop="past_college_title">
          <el-input
            v-model="form.past_college_title"
            disabled
            style="width: 300px"
          ></el-input>
        </el-form-item>
        <el-form-item label="原支部" prop="past_branch_title">
          <el-input
            v-model="form.past_branch_title"
            disabled
            style="width: 300px"
          ></el-input>
        </el-form-item>
        <el-form-item label="待转学院" prop="new_college">
          <el-select
            v-model="form.new_college"
            style="width: 300px"
            @change="changeSelect"
          >
            <el-option
              v-for="(item, index) in college"
              :key="index"
              :label="item.college_title"
              :value="item.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="待转支部" prop="new_branch">
          <el-select v-model="form.new_branch" style="width: 300px">
            <el-option
              v-for="(item, index) in typeOptions"
              :key="index"
              :label="item.branch_title"
              :value="item.id"
            />
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit_btn()">确 定</el-button>
      </div>
    </el-dialog>

    <el-table :data="tableData" style="width: 100%; margin-top: 20px" border>
      <el-table-column label="原学院" prop="past_college_t" align="center">
      </el-table-column>
      <el-table-column label="原支部" prop="past_branch_t" align="center">
      </el-table-column>
      <el-table-column label="新学院" prop="new_college_t" align="center">
      </el-table-column>
      <el-table-column label="新支部" prop="new_branch_t" align="center">
      </el-table-column>
      <el-table-column align="center" label="状态">
        <template slot-scope="scope">
          <div class="text" v-show="scope.row.state == '1'">申请中</div>
          <div class="text" v-show="scope.row.state == '2'">已通过</div>
          <div class="text" v-show="scope.row.state == '3'">申请失败</div>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            v-show="scope.row.state == '1'"
            >取消</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import a_downdialog from "../Cha_comp/a_downdialog.vue";
export default {
  props: {},
  components: {
    a_downdialog,
  },
  data() {
    return {
      tableData: [],
      show_text: false,
      search: "",
      dialogFormVisible: false,
      typeOptions: [],
      form: {
        account: "",
        past_college: "",
        past_branch: "",
        past_college_title: "",
        past_branch_title: "",
        new_college: "",
        new_branch: "",
        name: "",
        date: "",
      },
      rules: {
        new_college: [
          { required: true, message: "请选择学院", trigger: "change" },
        ],
        new_branch: [
          { required: true, message: "请选择支部", trigger: "change" },
        ],
      },
      college: [],
      branch: {},
    };
  },
  mounted() {
    this.showinformation();
    let tempdate;
    let year = new Date().getFullYear();
    let month = new Date().getMonth() + 1;
    let day = new Date().getDate();
    tempdate = year + "-" + month + "-" + day;
    this.form.date = tempdate;
    this.getmessage();
  },
  methods: {
     async getmessage() {
      const res = await this.$http.get("college/all");
      const temp= await this.$http.get("branch/all");
      this.college=res.data;
      this.branch=temp.data;
    },
    changeSelect() {
      // 清空支部内容
      this.form.branch = "";

      // 遍历学院的下拉选项数组
      for (const k in this.college) {
        // 学院内容 是否等于 学院的下拉选择数组中的某一项
        if (this.form.new_college === this.college[k].id) {
          for(const t in this.branch)
          {
            if(this.college[k].college_title==this.branch[t].college_title)
            {
              this.typeOptions.push(this.branch[t]);
            }
          }
        }
      }
    },
    async showinformation() {
      this.form.account = JSON.parse(localStorage.getItem("account"));
      console.log(this.account);
      const res = await this.$http.get(
        "transferorganization/get/" + this.form.account
      );
      console.log(res);
      this.form.past_college_title = res.data.college_title;
      this.form.past_branch_title = res.data.branch_title;
      this.form.past_college = res.data.college;
      this.form.past_branch = res.data.branch;
      this.form.name = JSON.parse(localStorage.getItem("name"));
      const res2 = await this.$http.get(
        "transferorganization/retrieve/" + this.form.account
      );
      console.log(res2);
      this.tableData = res2.data;
    },
    // changeSelect() {
    //   // 清空支部内容
    //   this.form.new_branch = "";
    //   // 遍历学院的下拉选项数组
    //   for (const k in this.college) {
    //     // 学院内容 是否等于 学院的下拉选择数组中的某一项
    //     console.log(this.form.new_college);
    //     console.log(this.college[k].id);
    //     if (this.form.new_college === this.college[k].id) {
    //       this.typeOptions = this.branch[this.college[k].label];
    //     }
    //   }
    // },
    async submit_btn() {
      console.log(this.form);
      const res = await this.$http.post(
        "transferorganization/create/",
        this.form
      );
      this.dialogFormVisible = false;
      console.log(res);
      if (res.data.entail != null) {
        this.$message.error(res.data.entail);
      } else {
        this.$message({
          message: "提交成功",
          type: "success",
        });
      }
    },
    async handleDelete(index, row) {
      // console.log(index, row);
      let temp2 = row.id;
      row.state = 3;
      console.log(temp2);
      console.log(row);
      const res3 = await this.$http.put(
        "transferorganization/update/" + temp2,
        row
      );
      console.log(res3);
      this.$message({
        message: "已不同意该申请",
        type: "success",
      });
    },
  },
};
</script>

<style>
.f {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: start;
  flex-direction: column;
}
.f_form {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.el-form-item__label {
  color: #303133;
  font-size: 14px;
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
}
</style>