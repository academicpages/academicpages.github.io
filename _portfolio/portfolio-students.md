---
title: "Portfolio-students" 
excerpt: "科研：难走的路才有好风景！ <br/><img src='/images/2493466.jpg' width='50%'>"
collection: portfolio
---

# 2024级

<table style="width: 100%; max-width: 800px;">
<tr>
  {% for student in students_2024 %}
  <td style="width: 25%; text-align: center;">
    <img src="{{ student.image }}" alt="{{ student.name }}" class="student-img" />
    <img src="{{ student.research }}" alt="科研" class="research-img" />
    <p>{{ student.graduation_destination }}</p>
  </td>
  {% endfor %}
</tr>
</table>

# 2023级

<table style="width: 100%; max-width: 800px;">
<tr>
  {% for student in students_2023 %}
  <td style="width: 50%; text-align: center;">
    <img src="{{ student.image }}" alt="{{ student.name }}" class="student-img" />
    <img src="{{ student.research }}" alt="科研" class="research-img" />
    <p>{{ student.graduation_destination }}</p>
  </td>
  {% endfor %}
</tr>
</table>

# 2022级

<table style="width: 100%; max-width: 800px;">
<tr>
  {% for student in students_2022 %}
  <td style="width: 33.33%; text-align: center;">
    <img src="{{ student.image }}" alt="{{ student.name }}" class="student-img" />
    <img src="{{ student.research }}" alt="科研" class="research-img" />
    <p>{{ student.graduation_destination }}</p>
  </td>
  {% endfor %}
</tr>
</table>

# 2021级

<table style="width: 100%; max-width: 800px;">
<tr>
  {% for student in students_2021 %}
  <td style="width: 50%; text-align: center;">
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img src="{{ student.image }}" alt="{{ student.name }}" class="student-img" />
      <img src="{{ student.research }}" alt="科研" class="research-img" />
      <p>{{ student.graduation_destination }}</p>
    </div>
  </td>
  {% endfor %}
</tr>
</table>

# 2020级

<table style="width: 50%; max-width: 400px;">
<tr>
  <td style="text-align: center;">
    <img src="{{ student.image }}" alt="{{ student.name }}" class="student-img" />
    <img src="{{ student.research }}" alt="科研" class="research-img" />
    <p>{{ student.graduation_destination }}</p>
  </td>
</tr>
</table>

# 合影

<table style="width: 100%; max-width: 800px;">
<tr>
  {% for photo in group_photos %}
  <td style="width: 50%; text-align: center;">
    <img src="{{ photo }}" alt="合影" class="group-photo" />
  </td>
  {% endfor %}
</tr>
</table>

<style>
.student-img {
max-width: 100%;
max-height: 200px;
object-fit: cover;
object-position: center;
}

.research-img {
max-width: 100%;
max-height: 100px;
object-fit: cover;
object-position: center;
}

.group-photo {
max-width: 100%;
max-height: 400px;
object-fit: cover;
object-position: center;
}
</style>