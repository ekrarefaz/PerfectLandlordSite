<template>

  <section>
    <div class="card">
      <p class="card-name">Bob<span>Head model</span></p>
      <div class="card-details">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis nostrum eum minus tenetur fugiat magnam, velit saepe impedit quo hic reprehenderit nihil debitis, voluptate veritatis vel quod aliquam nemo, quia harum similique. Pariatur eum officiis repellendus, quo tempore quibusdam aliquid? Sit atque laudantium odit reiciendis, aspernatur consequuntur doloremque libero.</p>
      </div>
    </div>
    <div class="card">
      <p class="card-name">Bob<span>Head model</span></p>
      <div class="card-details">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis nostrum eum minus tenetur fugiat magnam, velit saepe impedit quo hic reprehenderit nihil debitis, voluptate veritatis vel quod aliquam nemo, quia harum similique. Pariatur eum officiis repellendus, quo tempore quibusdam aliquid? Sit atque laudantium odit reiciendis, aspernatur consequuntur doloremque libero.</p>
      </div>
    </div>
    <!--   <div class="card">
      <p class="card-name">Bob<span>Mannequin chapeau</span></p>
      <div class="card-details">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis nostrum eum minus tenetur fugiat magnam, velit saepe impedit quo hic reprehenderit nihil debitis, voluptate veritatis vel quod aliquam nemo, quia harum similique. Pariatur eum officiis repellendus, quo tempore quibusdam aliquid? Sit atque laudantium odit reiciendis, aspernatur consequuntur doloremque libero.</p>
      </div>
    </div>
    <div class="card">
      <p class="card-name">Bob<span>Mannequin chapeau</span></p>
      <div class="card-details">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur perspiciatis nostrum eum minus tenetur fugiat magnam, velit saepe impedit quo hic reprehenderit nihil debitis, voluptate veritatis vel quod aliquam nemo, quia harum similique. Pariatur eum officiis repellendus, quo tempore quibusdam aliquid? Sit atque laudantium odit reiciendis, aspernatur consequuntur doloremque libero.</p>
      </div>
    </div> -->
  </section>
    
</template>

<style scoped >
@import url("https://fonts.googleapis.com/css?family=Montserrat:400,400i,700");

:root {
  --card-width: 250px;
  --space: 20px;
  --transition: 0.3s ease-out;
}

body {
  font-family: Montserrat;
}

section {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: var(--space);
  padding: var(--space);
}

.card {
  position: relative;
  width: var(--card-width);
  min-height: 300px;
  padding: var(--space);
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  border-radius: 10px;
  cursor: pointer;
  overflow: hidden;
  font-size: 1.5rem;
  color: #ffffff;
  text-align: right;
  background: url("https://images.unsplash.com/photo-1532123675048-773bd75df1b4?crop=entropy&cs=tinysrgb&fm=jpg&ixid=MnwzMjM4NDZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NzU4MDUxODQ&ixlib=rb-4.0.3&w=350")
    0 / cover no-repeat;
  transition: width var(--transition);
}

.card p {
  user-select: none;
}

.card-name span {
  display: block;
  font-size: 1rem;
}

.card-details {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  padding: calc(var(--space) * 2);
  color: #ffffff;
  text-align: left;
  font-size: 1.2rem;
  clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  background-color: rgba(214, 47, 41, 0.845);
  transition: clip-path var(--transition);
}

.card-details p {
  text-overflow: ellipsis;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 8;
  -webkit-box-orient: vertical;
  white-space: normal;
}

.card.active .card-details {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}

.active {
  width: calc(var(--card-width) * 2);
}

</style>