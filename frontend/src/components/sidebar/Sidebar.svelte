<script lang="ts">
  import BackToOw from "./BackToOW.svelte";
  import UserFilters from "../filters/checkboxes/UserFilters.svelte";
  import GroupPicker from "./GroupPicker.svelte";
  import Logout from "./Logout.svelte";
  import PunishmentsFilters from "../filters/punishments/PunishmentsFilters.svelte";
  import SearchUser from "./SearchUser.svelte";
  import DateTimeFilters from "../filters/time/DateTimeFilters.svelte";
  import VvLogo from "./VvLogo.svelte";
</script>

<div class="wrapper h-auto">
  <div class="flex flex-col h-auto">
    <VvLogo />
    <GroupPicker />

    <SearchUser />

    <PunishmentsFilters />

    <DateTimeFilters />

    <UserFilters />

    <div class="mt-8 flex flex-col">
      <BackToOw />
      <Logout />
    </div>
  </div>
</div>

<style lang="less">
  .wrapper {
    width: 25rem;
    display: flex;
    flex-direction: column;
    background: #153e75;
    box-sizing: border-box;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    padding-bottom: 1rem;
  }
</style>
