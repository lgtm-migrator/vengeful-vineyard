<script lang="ts">
  import { group } from "../../../stores/group";
  import PunishmentTag from "./PunishmentTag.svelte";
  import { punishmentsToFilter } from "../../../stores/punishmentToFilter";
  import PunishmentTagSelect from "./PunishmentTagSelect.svelte";

  const resetPunishmentFilters = (): void => {
    punishmentsToFilter.set($group.punishment_types);
  };

  $: showAll = $group
    ? $punishmentsToFilter
        ?.map((pun) => pun.punishment_type_id)
        .sort()
        .join(",") ===
      $group.punishment_types
        ?.map((pun) => pun.punishment_type_id)
        .sort()
        .join(",")
    : true;
</script>

{#if $punishmentsToFilter}
  <div class="wrapper">
    <div class="punishmentTags">
      {#each $punishmentsToFilter as punishment}
        <PunishmentTag punishment="{punishment}" />
      {/each}
    </div>
    <PunishmentTagSelect />

    <div class="form-control">
      <label class="cursor-pointer label">
        <input
          type="checkbox"
          bind:checked="{showAll}"
          class="checkbox checkbox-secondary"
          disabled="{showAll}"
          on:click="{() => resetPunishmentFilters()}"
        />
        <span class="label-text">Vis alle</span>
      </label>
    </div>
  </div>
{/if}

<style lang="less">
  .wrapper {
    padding: 0rem 1.5rem;
  }

  .punishmentTags {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap-reverse;
  }

  .label-text {
    color: #eeeeee;
    font-size: 16px;
    float: left;
    padding-left: 5px;
  }

  .label {
    display: flex;
    justify-content: left;
    width: fit-content;
  }

  .checkbox {
    width: 1.1rem;
    height: 1.1rem;
    border-radius: 6px;
  }
</style>
