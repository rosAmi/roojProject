<template>
    <div id="resolve">
      {{msg}}

    </div>
</template>

<script>

export default {
  name: "Resolve",
  data() {
    return {
      msg: ' Resolve of issue: '
    }
  },
  methods: {
  
  }
};
</script>

<style scoped>
p {
  font-size: 18px;
}

form.form-ui {
  display: table;
  margin: 15px;
}

div.form-ui {
  display: table-row;
}

label,
input {
  display: table-cell;
  margin-bottom: 10px;
}

label {
  padding-right: 10px;
}

</style>