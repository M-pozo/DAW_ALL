-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql
-- Tiempo de generación: 08-11-2023 a las 16:27:18
-- Versión del servidor: 5.7.43
-- Versión de PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `portfolio_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nombre` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`) VALUES
(1, 'PHP'),
(2, 'JavaScript'),
(3, 'Java'),
(4, 'HTML'),
(5, 'CSS'),
(6, 'Python');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_proyecto`
--

CREATE TABLE `categoria_proyecto` (
  `id` int(11) NOT NULL,
  `proyecto_id` int(11) NOT NULL,
  `categoria_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `categoria_proyecto`
--

INSERT INTO `categoria_proyecto` (`id`, `proyecto_id`, `categoria_id`) VALUES
(1, 1, 4),
(2, 1, 5),
(3, 2, 6),
(4, 2, 2),
(5, 3, 4),
(6, 3, 5),
(7, 4, 3),
(8, 4, 6),
(9, 5, 4),
(10, 5, 1),
(11, 5, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `id` int(11) NOT NULL,
  `nombre y apellidos` text NOT NULL,
  `e-mail` varchar(50) NOT NULL,
  `telefono` int(11) NOT NULL,
  `particular/empresa` text NOT NULL,
  `mensaje` text NOT NULL,
  `archivo` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`id`, `nombre y apellidos`, `e-mail`, `telefono`, `particular/empresa`, `mensaje`, `archivo`) VALUES
(1, 'Pepe', 'pepe@gmail.com', 652658745, 'particular', '33', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `id` int(11) NOT NULL,
  `clave` varchar(50) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `fecha` date NOT NULL,
  `descripcion` text NOT NULL,
  `imagen` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`id`, `clave`, `titulo`, `fecha`, `descripcion`, `imagen`) VALUES
(1, 'proyecto1', 'Porfolio', '2023-10-24', 'Mostrar todos mis proyectos', 'static\\/images\\/proyecto1.jpg'),
(2, 'proyecto2', 'Torneo', '2022-11-14', 'Utilizar la API de un juego para coger los datos de los participantes', 'static\\/images\\/torneo.png'),
(3, 'proyecto3', 'MyFilms', '2023-11-14', 'Almacenar y categorizar pel\\u00edculas seg\\u00fan mis rese\\u00f1as', 'static\\/images\\/pelicula.png'),
(4, 'proyecto4', 'Juego 2D', '2020-11-14', 'Juego web 2D de plataformas', 'static\\/images\\/juego2d.png'),
(5, 'proyecto5', 'Ropa', '2019-11-14', 'Venta de ropa de segunda mano', 'static\\/images\\/ropa.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sesion`
--

CREATE TABLE `sesion` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` text NOT NULL,
  `nombreApellidos` text NOT NULL,
  `dni` text NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT '1',
  `admin` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `email`, `password`, `nombreApellidos`, `dni`, `activo`, `admin`) VALUES
(1, 'prueba@gmail.com', '1234', 'Miguel Pozo PÃ©rez', '15236598L', 1, 0),
(2, 'miguel@gmail.com', '123', 'Miguel Pozo Pérez', '51236548I', 1, 1),
(3, 'pepe@gmail.com', '123', 'Pepe Alonso Ronaldo', '45896523K', 1, 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `categoria_proyecto`
--
ALTER TABLE `categoria_proyecto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_categoria` (`categoria_id`),
  ADD KEY `fk_proyecto` (`proyecto_id`);

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `clave` (`clave`),
  ADD UNIQUE KEY `titulo` (`titulo`);

--
-- Indices de la tabla `sesion`
--
ALTER TABLE `sesion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_usuario` (`usuario_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria_proyecto`
--
ALTER TABLE `categoria_proyecto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `sesion`
--
ALTER TABLE `sesion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `categoria_proyecto`
--
ALTER TABLE `categoria_proyecto`
  ADD CONSTRAINT `fk_categoria` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`),
  ADD CONSTRAINT `fk_proyecto` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`id`);

--
-- Filtros para la tabla `sesion`
--
ALTER TABLE `sesion`
  ADD CONSTRAINT `fk_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
