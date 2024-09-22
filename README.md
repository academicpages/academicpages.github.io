
# Academic Pages

![pages-build-deployment](https://github.com/academicpages/academicpages.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)

Academic Pages is a Github Pages template for academic websites.


# Getting Started

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Click the "Use this template" button in the top right.
1. On the "New repository" page, enter your repository name as "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and add your content.
1. Upload any files (like PDFs, .zip files, etc.) to the `files/` directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## Running Locally

When you are initially working your website, it is very useful to be able to preview the changes locally before pushing them to GitHub. To work locally you will need to:

1. Clone the repository and made updates as detailed above.
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `jekyll serve -l -H localhost` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.


# Maintenance 

Bug reports and feature requests to the template  should be [submitted via GitHub](https://github.com/academicpages/academicpages.github.io/issues/new/choose). For questions concerning how to style the template, please feel free to start a [new discussion on GitHub](https://github.com/academicpages/academicpages.github.io/discussions).

This repository was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License (see LICENSE.md). It is currently being maintained by [Robert Zupko](https://github.com/rjzupkoii) and additional maintainers would be welcomed.

## Bugfixes and enhancements

If you have bugfixes and enhancements that you would like to submit as a pull request, you will need to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repository as opposed to using it as a template. This will also allow you to [synchronize your copy](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) of template to your fork as well.

Unfortunately, one logistical issue with a template theme like Academic Pages that makes it a little tricky to get bug fixes and updates to the core theme. If you use this template and customize it, you will probably get merge conflicts if you attempt to synchronize. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch.

# Capítulo 4: Método de Runge-Kutta de Cuarto Orden

## 4.1. Introducción

El método de Runge-Kutta de cuarto orden es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDOs) de la forma:

$$
\frac{dy}{dt} = f(t, y)
$$

El método es particularmente útil debido a su precisión y simplicidad. La fórmula básica para avanzar desde el punto \( t_n \) hasta \( t_{n+1} \) con un paso \( h \) es:

$$
y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

donde:

\[
\begin{align*}
k_1 &= h f(t_n, y_n) \\
k_2 &= h f\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right) \\
k_3 &= h f\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right) \\
k_4 &= h f(t_n + h, y_n + k_3)
\end{align*}
\]

## 4.2. Implementación en Fortran

A continuación se muestra una implementación del método de Runge-Kutta de cuarto orden en Fortran para resolver la EDO:

$$
\frac{dy}{dt} = -2ty
$$

con la condición inicial \( y(0) = 1 \).

### Código Fortran

```fortran
! Archivo: runge_kutta.f90
PROGRAM RungeKutta4

  IMPLICIT NONE
  REAL :: t, y, h
  INTEGER :: i, n

  ! Definición de variables
  REAL, PARAMETER :: t0 = 0.0, y0 = 1.0, tf = 5.0, h_step = 0.1
  INTEGER, PARAMETER :: n_steps = INT((tf - t0) / h_step)

  ! Inicialización
  t = t0
  y = y0

  ! Impresión de la condición inicial
  PRINT *, 't = ', t, ' y = ', y

  ! Iteración del método de Runge-Kutta de cuarto orden
  DO i = 1, n_steps
     CALL RungeKuttaStep(t, y, h_step)
     PRINT *, 't = ', t, ' y = ', y
  END DO

CONTAINS

  ! Subrutina para un paso de Runge-Kutta de cuarto orden
  SUBROUTINE RungeKuttaStep(t, y, h)
    REAL, INTENT(INOUT) :: t, y
    REAL, INTENT(IN) :: h
    REAL :: k1, k2, k3, k4

    ! Cálculo de los coeficientes k1, k2, k3 y k4
    k1 = h * f(t, y)
    k2 = h * f(t + 0.5*h, y + 0.5*k1)
    k3 = h * f(t + 0.5*h, y + 0.5*k2)
    k4 = h * f(t + h, y + k3)

    ! Actualización de y y t
    y = y + (1.0 / 6.0) * (k1 + 2.0*k2 + 2.0*k3 + k4)
    t = t + h

  END SUBROUTINE RungeKuttaStep

  ! Función para la EDO
  REAL FUNCTION f(t, y)
    REAL, INTENT(IN) :: t, y
    f = -2.0 * t * y
  END FUNCTION f

END PROGRAM RungeKutta4
