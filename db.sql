//存储用例
CREATE TABLE `sniffer_cases` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增长ID',
  `casename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `create_by` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `system` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT ' 所属系统',
  `url` varchar(164) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT ' 发起url',
  `data` text COLLATE utf8mb4_unicode_ci COMMENT '发起数据',
  `method` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expect` text COLLATE utf8mb4_unicode_ci,
  `emailto` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `create_at` bigint(20) NOT NULL COMMENT '数据创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
//用例执行结果

CREATE TABLE `sniffer_result` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增长ID',
  `cases_id` bigint(20) NOT NULL COMMENT '用例id',
  `casename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `create_by` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `system` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT ' 所属系统',
  `request` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT ' 发起请求',
  `method` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `return_result` text COLLATE utf8mb4_unicode_ci COMMENT ' 实际返回结果',
  `result` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT ' 用例结果',
  `create_at` bigint(20) NOT NULL COMMENT '数据创建时间',
  `run_count` bigint(20) NOT NULL COMMENT '执行第多少次',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci


CREATE TABLE `quality_service` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增长ID',
  `info` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ques_from` varchar(100) COLLATE utf8mb4_unicode_ci NOT null COMMENT'反馈人',
  `ques_system` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '所属系统',
  `ques_dsc` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '问题描述',
  `ques_to` varchar(100) COLLATE utf8mb4_unicode_ci COMMENT '问题接收人',
  `ques_result` text COLLATE utf8mb4_unicode_ci NOT null COMMENT '处理结果',
  `ques_status` varchar(64) COLLATE utf8mb4_unicode_ci COMMENT '是否解决',
  `is_bug` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT null COMMENT '是否为bug',
  `create_at` varchar(64) NOT NULL COMMENT '数据创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
