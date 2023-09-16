<script>
import SidebarLink from './SidebarLink'
import { collapsed, togglesidebar, sidebarWidth } from './state'

export default {
    props: {},
    components: { 
        SidebarLink 
    },
    setup() {
        return { collapsed, togglesidebar, sidebarWidth}
    }
}

</script>

<template>
    <div class="sidebar" :style="{ width: sidebarWidth }">
        <img class="profile-pic"
        src="@/assets/logo.png"  
        alt="User Image"/>
        <div class="link">
            <SidebarLink to="/" icon="fas fa-home">Home</SidebarLink>
            <SidebarLink to="/dashboard" icon="fas fa-columns">Dashboard</SidebarLink>
            <SidebarLink to="/analytics" icon="fas fa-chart-bar">Analytics</SidebarLink>
            <SidebarLink to="/friends" icon="fas fa-users">Friends</SidebarLink>
            <SidebarLink to="/image" icon="fas fa-image">Images</SidebarLink>
        </div>


        <span class="collapse-icon" 
        :class="{ 'rotate-180': collapsed}"
        @click="togglesidebar">
            <i class="fas fa-angle-double-left" />
        </span>
    </div>
</template>



<style>
:root {
    --sidebar-bg-color: #333;
    --sidebar-item-hover: #007c7d;
    --sidebar-item-active: #006769;
}
</style>

<style scoped>

.link {
    margin-top: 2em;
}
.sidebar {
    color: white;
    background-color: var(--sidebar-bg-color);
    
    float: left;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    bottom: 0;
    padding: 0.5em;

    transition: 0.3s ease;

    display: flex;
    flex-direction: column;
}

.profile-pic {
    border-radius: 50%;
    width: 100%;
    max-width: 5em;
    height: auto;
    object-fit: cover;

}
.collapse-icon {
    position: absolute;
    /* top: 100; */
    bottom: 0;
    padding: 0.75em;

    color: #faf9f6;

    transition: 0.2s linear;
}

.rotate-180 {
    transform: rotate(180deg);
    transition: 0.2s linear;
}

</style>