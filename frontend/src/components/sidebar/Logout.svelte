<script lang="ts">
  import { LogoutButton, isAuthenticated } from "@dopry/svelte-oidc";
</script>

<div class="flex m-auto pt-5">
  {#if $isAuthenticated}
    <div class="w-full m-auto hover:bg-red-600 rounded-lg">
      <div class="btn bg-red-500 rounded-lg ">
        <LogoutButton>Logg ut</LogoutButton>
      </div>
    </div>
  {/if}
</div>

<style lang="postcss">
  .btn {
    width: fit-content;
    padding: 0;
  }
</style>
