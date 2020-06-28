<template>
  <div class="home">
    <budget-summary></budget-summary>
  </div>
</template>

<script>

import BudgetSummary from "@/components/BudgetSummary.vue";

export default {
  name: "Home",
  components: {
    BudgetSummary
  }
};
</script>
