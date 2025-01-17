import { writable } from 'svelte/store'
import type { Group } from '../lib/types'

export const group = writable<Group>(JSON.parse(localStorage.getItem('group')))

group.subscribe(value => (localStorage.group = JSON.stringify(value)))
