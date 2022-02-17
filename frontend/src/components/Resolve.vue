<template>
    <div>


    </div>
</template>

<script>

export default {
  name: "Resolve",
  data() {
    return {
      id: '',
      problem: '',
      serial: '',
      indicator1: '',
      indicator2: '',
      indicator3: ''
    };
  },
  methods: {
    createForm() {
    // POST request using axios with error handling
    const formData = { 
          id: this.id,
          problem: this.problem,
          serial: this.serial,
          indicator1: this.indicator1,
          indicator2: this.indicator2,
          indicator3: this.indicator3
           };
    axios.post("http://localhost:3001/1", formData) // "https://reqres.in/api/articles"
      .then(response => console.log(response))
      //.then(response => this.formDataId = response.data.id)
      .catch(error => {
        this.errorMessage = error.message;
        console.error("There was an error!", error);
      });
    }
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

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>