-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql
-- Tiempo de generación: 23-10-2023 a las 15:47:19
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_proyecto`
--

CREATE TABLE `categoria_proyecto` (
  `id` int(11) NOT NULL,
  `proyecto` int(11) NOT NULL,
  `categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  `imagen` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sesion`
--

CREATE TABLE `sesion` (
  `id` int(11) NOT NULL,
  `usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `e-mail` varchar(50) NOT NULL,
  `password` text NOT NULL,
  `nombre y apellido` text NOT NULL,
  `dni` text NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT '1',
  `admin` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  ADD KEY `fk_categoria` (`categoria`),
  ADD KEY `fk_proyecto` (`proyecto`);

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
  ADD KEY `fk_usuario` (`usuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `categoria_proyecto`
--
ALTER TABLE `categoria_proyecto`
  ADD CONSTRAINT `fk_categoria` FOREIGN KEY (`categoria`) REFERENCES `categoria` (`id`),
  ADD CONSTRAINT `fk_proyecto` FOREIGN KEY (`proyecto`) REFERENCES `proyecto` (`id`);

--
-- Filtros para la tabla `sesion`
--
ALTER TABLE `sesion`
  ADD CONSTRAINT `fk_usuario` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
