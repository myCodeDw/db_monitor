from django.db import models
from django.utils import timezone

class MysqlStat(models.Model):
    tags = models.CharField("标签",max_length=32)
    host = models.CharField("主机ip",max_length=32)
    port = models.IntegerField("数据库端口号",default=1521)
    version = models.CharField("数据库版本",max_length=64,blank=True,null=True)
    updays = models.IntegerField("运行天数",blank=True,null=True)
    basedir = models.CharField("MySQL路径",max_length=255,blank=True,null=True)
    datadir = models.CharField("数据存放路径",max_length=255,blank=True,null=True)
    slow_query_log = models.CharField("慢查询日志是否开启",max_length=32,blank=True,null=True)
    slow_query_log_file = models.CharField("慢查询日志路径",max_length=255,blank=True,null=True)
    log_bin = models.CharField("binlog是否开启",max_length=255,blank=True,null=True)
    max_connections = models.IntegerField("最大连接数",blank=True,null=True)
    max_connect_errors = models.IntegerField("最大错误连接数",blank=True,null=True)
    total_rows = models.FloatField("数据库总大小(GB)",blank=True, null=True)
    data_size = models.FloatField("数据大小(GB)",blank=True, null=True)
    index_size = models.FloatField("索引大小(GB)",blank=True, null=True)
    threads_connected = models.IntegerField("连接线程数",blank=True,null=True)
    threads_running = models.IntegerField("运行线程数",blank=True,null=True)
    threads_waited = models.IntegerField("等待线程数",blank=True,null=True)
    threads_created = models.IntegerField("创建线程数",blank=True,null=True)
    threads_cached = models.IntegerField("缓存线程数",blank=True,null=True)
    qps = models.IntegerField("每秒查询请求数",blank=True, null=True)
    tps = models.IntegerField("每秒事务处理数",blank=True, null=True)
    bytes_received = models.FloatField("每秒接收数量(KB)",blank=True, null=True)
    bytes_sent = models.FloatField("每秒发送字数量(KB)",blank=True, null=True)
    open_files_limit = models.IntegerField("最大打开文件数量",blank=True, null=True)
    open_files = models.IntegerField("打开文件数量",blank=True, null=True)
    table_open_cache = models.IntegerField("最大打开表数量",blank=True, null=True)
    open_tables = models.IntegerField("打开表数量",blank=True, null=True)
    key_buffer_size = models.FloatField("索引缓冲区大小",blank=True,null=True)
    sort_buffer_size = models.FloatField("排序缓冲区大小",blank=True,null=True)
    join_buffer_size = models.FloatField("连接缓冲区大小",blank=True,null=True)
    key_blocks_unused = models.IntegerField("未使用的缓冲block数量",blank=True, null=True)
    key_blocks_used = models.IntegerField("已使用的缓冲block数量",blank=True, null=True)
    key_blocks_not_flushed = models.IntegerField("已更改但还未更新到硬盘的键数量",blank=True, null=True)
    mysql_sel = models.IntegerField("查询语句数量",blank=True,null=True)
    mysql_ins = models.IntegerField("插入语句数量",blank=True,null=True)
    mysql_upd = models.IntegerField("更新语句数量",blank=True,null=True)
    mysql_del = models.IntegerField("删除语句数量",blank=True,null=True)
    select_scan = models.IntegerField("全表扫描数量",blank=True,null=True)
    slow_queries = models.IntegerField("慢查询语句数量",blank=True,null=True)
    key_read_requests = models.IntegerField("从缓存读取索引的请求次数",blank=True,null=True)
    key_reads = models.IntegerField("从磁盘读取索引的请求次数",blank=True,null=True)
    key_write_requests = models.IntegerField("通过缓存写索引的请求次数",blank=True,null=True)
    key_writes = models.IntegerField("通过磁盘写索引的请求次数",blank=True,null=True)
    innodb_buffer_pool_size = models.FloatField("innodb缓冲池大小(字节)",blank=True,null=True)
    innodb_buffer_pool_pages_total = models.IntegerField("innodb缓冲池大小(页数量)",blank=True,null=True)
    innodb_buffer_pool_pages_data = models.IntegerField("innodb缓冲池中数据页数量(包括脏页)",blank=True,null=True)
    innodb_buffer_pool_pages_dirty = models.IntegerField("innodb缓冲池中脏页数量",blank=True,null=True)
    innodb_buffer_pool_pages_free = models.IntegerField("innodb缓冲池中剩余页数量",blank=True,null=True)
    innodb_buffer_pool_hit = models.FloatField("innodb缓冲池缓存命中率",blank=True,null=True)
    innodb_io_capacity = models.IntegerField("从缓冲区刷新脏页时一次刷新的数量",blank=True,null=True)
    innodb_read_io_threads = models.IntegerField("innodb读线程数量",blank=True,null=True)
    innodb_write_io_threads = models.IntegerField("innodb写线程数量",blank=True,null=True)
    innodb_rows_deleted = models.IntegerField("innodb每秒删除的行数",blank=True,null=True)
    innodb_rows_inserted = models.IntegerField("innodb每秒插入的行数",blank=True,null=True)
    innodb_rows_read = models.IntegerField("innodb每秒读取的行数",blank=True,null=True)
    innodb_rows_updated = models.IntegerField("innodb每秒更新的行数",blank=True,null=True)
    innodb_row_lock_waits = models.IntegerField("innodb启动到现在总共等待的次数",blank=True,null=True)
    innodb_row_lock_time_avg = models.FloatField("每次等待所花费平均时间",blank=True,null=True)
    innodb_buffer_pool_pages_flushed = models.IntegerField("innodb脏页刷新的频率",blank=True,null=True)
    innodb_data_read = models.FloatField("innodb读取的数据量",blank=True,null=True)
    innodb_data_written = models.FloatField("innodb写入的数据量",blank=True,null=True)
    innodb_data_reads = models.IntegerField("innodb读请求次数",blank=True,null=True)
    innodb_data_writes = models.IntegerField("innodb写请求次数",blank=True,null=True)
    innodb_log_writes = models.IntegerField("innodb日志写入次数",blank=True,null=True)
    innodb_data_fsyncs = models.IntegerField("数据刷新次数",blank=True,null=True)
    innodb_os_log_written = models.FloatField("innodb写入redo log的字节数",blank=True,null=True)
    status = models.IntegerField("数据库连接状态 0成功 1失败",blank=True, null=True)
    check_time = models.DateTimeField("采集时间",default=timezone.now,blank=True, null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'mysql_stat'
        verbose_name = "mysql数据库采集数据"
        verbose_name_plural = verbose_name


class MysqlSlowquery(models.Model):
    tags = models.CharField("标签",max_length=256)
    host = models.CharField("主机ip",max_length=32)
    start_time  = models.CharField("执行时间",max_length=64)
    client_host = models.CharField("主机信息",max_length=64)
    db_name = models.CharField("数据库名",max_length=64)
    sql_text = models.TextField("sql文本")
    query_time = models.FloatField("执行耗时(秒)")
    lock_time = models.FloatField("锁等待时间(秒)")
    rows_examined = models.IntegerField("扫描行数",blank=True, null=True)
    rows_sent = models.IntegerField("返回客户端行数",blank=True, null=True)
    thread_id = models.CharField("线程号",max_length=64)
    check_time = models.DateTimeField("采集时间",default=timezone.now,blank=True, null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'mysql_slowquery'
        verbose_name = "mysql慢查询采集数据"
        verbose_name_plural = verbose_name


class MysqlStatHis(models.Model):
    tags = models.CharField("标签",max_length=32)
    host = models.CharField("主机ip",max_length=32)
    port = models.IntegerField("数据库端口号",default=1521)
    version = models.CharField("数据库版本",max_length=64,blank=True,null=True)
    updays = models.IntegerField("运行天数",blank=True,null=True)
    basedir = models.CharField("MySQL路径",max_length=255,blank=True,null=True)
    datadir = models.CharField("数据存放路径",max_length=255,blank=True,null=True)
    slow_query_log = models.CharField("慢查询日志是否开启",max_length=32,blank=True,null=True)
    slow_query_log_file = models.CharField("慢查询日志路径",max_length=255,blank=True,null=True)
    log_bin = models.CharField("binlog是否开启",max_length=255,blank=True,null=True)
    max_connections = models.IntegerField("最大连接数",blank=True,null=True)
    max_connect_errors = models.IntegerField("最大错误连接数",blank=True,null=True)
    total_rows = models.FloatField("数据库总大小(GB)",blank=True, null=True)
    data_size = models.FloatField("数据大小(GB)",blank=True, null=True)
    index_size = models.FloatField("索引大小(GB)",blank=True, null=True)
    threads_connected = models.IntegerField("连接线程数",blank=True,null=True)
    threads_running = models.IntegerField("运行线程数",blank=True,null=True)
    threads_waited = models.IntegerField("等待线程数",blank=True,null=True)
    threads_created = models.IntegerField("创建线程数",blank=True,null=True)
    threads_cached = models.IntegerField("缓存线程数",blank=True,null=True)
    qps = models.IntegerField("每秒查询请求数",blank=True, null=True)
    tps = models.IntegerField("每秒事务处理数",blank=True, null=True)
    bytes_received = models.FloatField("每秒接收数量(KB)",blank=True, null=True)
    bytes_sent = models.FloatField("每秒发送字数量(KB)",blank=True, null=True)
    open_files_limit = models.IntegerField("最大打开文件数量",blank=True, null=True)
    open_files = models.IntegerField("打开文件数量",blank=True, null=True)
    table_open_cache = models.IntegerField("最大打开表数量",blank=True, null=True)
    open_tables = models.IntegerField("打开表数量",blank=True, null=True)
    key_buffer_size = models.FloatField("索引缓冲区大小",blank=True,null=True)
    sort_buffer_size = models.FloatField("排序缓冲区大小",blank=True,null=True)
    join_buffer_size = models.FloatField("连接缓冲区大小",blank=True,null=True)
    key_blocks_unused = models.IntegerField("未使用的缓冲block数量",blank=True, null=True)
    key_blocks_used = models.IntegerField("已使用的缓冲block数量",blank=True, null=True)
    key_blocks_not_flushed = models.IntegerField("已更改但还未更新到硬盘的键数量",blank=True, null=True)
    mysql_sel = models.IntegerField("查询语句数量",blank=True,null=True)
    mysql_ins = models.IntegerField("插入语句数量",blank=True,null=True)
    mysql_upd = models.IntegerField("更新语句数量",blank=True,null=True)
    mysql_del = models.IntegerField("删除语句数量",blank=True,null=True)
    select_scan = models.IntegerField("全表扫描数量",blank=True,null=True)
    slow_queries = models.IntegerField("慢查询语句数量",blank=True,null=True)
    key_read_requests = models.IntegerField("从缓存读取索引的请求次数",blank=True,null=True)
    key_reads = models.IntegerField("从磁盘读取索引的请求次数",blank=True,null=True)
    key_write_requests = models.IntegerField("通过缓存写索引的请求次数",blank=True,null=True)
    key_writes = models.IntegerField("通过磁盘写索引的请求次数",blank=True,null=True)
    innodb_buffer_pool_size = models.FloatField("innodb缓冲池大小(字节)",blank=True,null=True)
    innodb_buffer_pool_pages_total = models.IntegerField("innodb缓冲池大小(页数量)",blank=True,null=True)
    innodb_buffer_pool_pages_data = models.IntegerField("innodb缓冲池中数据页数量(包括脏页)",blank=True,null=True)
    innodb_buffer_pool_pages_dirty = models.IntegerField("innodb缓冲池中脏页数量",blank=True,null=True)
    innodb_buffer_pool_pages_free = models.IntegerField("innodb缓冲池中剩余页数量",blank=True,null=True)
    innodb_buffer_pool_hit = models.FloatField("innodb缓冲池缓存命中率",blank=True,null=True)
    innodb_io_capacity = models.IntegerField("从缓冲区刷新脏页时一次刷新的数量",blank=True,null=True)
    innodb_read_io_threads = models.IntegerField("innodb读线程数量",blank=True,null=True)
    innodb_write_io_threads = models.IntegerField("innodb写线程数量",blank=True,null=True)
    innodb_rows_deleted = models.IntegerField("innodb每秒删除的行数",blank=True,null=True)
    innodb_rows_inserted = models.IntegerField("innodb每秒插入的行数",blank=True,null=True)
    innodb_rows_read = models.IntegerField("innodb每秒读取的行数",blank=True,null=True)
    innodb_rows_updated = models.IntegerField("innodb每秒更新的行数",blank=True,null=True)
    innodb_row_lock_waits = models.IntegerField("innodb启动到现在总共等待的次数",blank=True,null=True)
    innodb_row_lock_time_avg = models.FloatField("每次等待所花费平均时间",blank=True,null=True)
    innodb_buffer_pool_pages_flushed = models.IntegerField("innodb脏页刷新的频率",blank=True,null=True)
    innodb_data_read = models.FloatField("innodb读取的数据量",blank=True,null=True)
    innodb_data_written = models.FloatField("innodb写入的数据量",blank=True,null=True)
    innodb_data_reads = models.IntegerField("innodb读请求次数",blank=True,null=True)
    innodb_data_writes = models.IntegerField("innodb写请求次数",blank=True,null=True)
    innodb_log_writes = models.IntegerField("innodb日志写入次数",blank=True,null=True)
    innodb_data_fsyncs = models.IntegerField("数据刷新次数",blank=True,null=True)
    innodb_os_log_written = models.FloatField("innodb写入redo log的字节数",blank=True,null=True)
    status = models.IntegerField("数据库连接状态 0成功 1失败",blank=True, null=True)
    check_time = models.DateTimeField("采集时间",default=timezone.now,blank=True, null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'mysql_stat_his'
        verbose_name = "mysql数据库采集数据"
        verbose_name_plural = verbose_name
