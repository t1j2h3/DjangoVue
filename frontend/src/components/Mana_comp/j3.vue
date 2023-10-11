<template>
  <div class="j3">
    <el-table :data="tables" style="width: 100%" border height="540" stripe>
      <el-table-column label="学号" prop="account" width="150px"> </el-table-column>
      <el-table-column label="姓名" prop="name" width="150px"> </el-table-column>
      <el-table-column label="学院" prop="college_title"> </el-table-column>
      <el-table-column label="班级" prop="branch_title"> </el-table-column>
      <el-table-column align="right" style=" display: flex;justify-content: center;  align-items: center;">
        <template slot="header" slot-scope="scope">
          <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
        </template>
        <template slot-scope="scope" style=" display: flex;justify-content: center;  align-items: center;">
          <el-button
            size="mini"
            style="  display: flex;justify-content: center;  align-items: center;"
            @click="pwdreset(scope.$index, scope.row)"
            >重置密码</el-button
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
      tableData: [],
      search: "",
    };
  },
  computed: {
    tables() {
      let search = this.search.toLowerCase();
      if (search) {
        // tableData是要放在表格中展示的数据
        return this.tableData.filter((data) => {
          // 获取对象数组的所有枚举属性，通过some来判断对象中的某一属性是否匹配上，如果匹配上了那么这个对象后面的属性就不用判断了，从而返回整个对象(毕竟我们要看整个对象的值)。
          return Object.keys(data).some((key) => {
            if (data[key] !== null)
              // 对象的属性不为空才进行模糊匹配，否则会报错
              return data[key].toString().toLowerCase().indexOf(search) > -1;
          });
        });
      } else {
        return this.tableData; // 如果搜索框没有值，就正常展示表格的所有数据
      }
    },
  },
  mounted() {
    this.showmessage();
  },
  methods: {
    async showmessage() {
      const val = JSON.parse(localStorage.getItem("id"));
      if (val == 2) {
        const val1 = JSON.parse(localStorage.getItem("from_branch"));
        const res = await this.$http.get("user/branch_all/" + val1);
        this.tableData = res.data;
      }
    },
    async pwdreset(index,row)
    {
        const res=await this.$http.post('user/pwdreset/'+row.account);
        if(res.status==200)
        {
            this.$message.success("密码重置成功");
        }
        else
        {
            this.$message.error(res.data.entail);
        }
    }
  },
};
</script>

<style>
.j3 {
  width: 100%;
  height: 100%;
}
.text {
  display: flex;
  justify-content: center;
}
/* .cell{
    display: flex;
    justify-content: center;
    align-items: center;
} */
</style>
