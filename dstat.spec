#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dstat
Version  : 0.7.2
Release  : 10
URL      : http://dag.wieers.com/home-made/dstat/dstat-0.7.2.tar.bz2
Source0  : http://dag.wieers.com/home-made/dstat/dstat-0.7.2.tar.bz2
Summary  : Pluggable real-time performance monitoring tool
Group    : Development/Tools
License  : GPL-2.0
Requires: dstat-bin
Requires: dstat-data
Requires: dstat-doc

%description
Dstat is a versatile replacement for vmstat, iostat, netstat and ifstat.
Dstat overcomes some of their limitations and adds some extra features,
more counters and flexibility. Dstat is handy for monitoring systems
during performance tuning tests, benchmarks or troubleshooting.

Dstat allows you to view all of your system resources in real-time, you
can eg. compare disk utilization in combination with interrupts from your
IDE controller, or compare the network bandwidth numbers directly
with the disk throughput (in the same interval). 

Dstat gives you detailed selective information in columns and clearly
indicates in what magnitude and unit the output is displayed. Less
confusion, less mistakes. And most importantly, it makes it very easy
to write plugins to collect your own counters and extend in ways you
never expected.

%package bin
Summary: bin components for the dstat package.
Group: Binaries
Requires: dstat-data

%description bin
bin components for the dstat package.


%package data
Summary: data components for the dstat package.
Group: Data

%description data
data components for the dstat package.


%package doc
Summary: doc components for the dstat package.
Group: Documentation

%description doc
doc components for the dstat package.


%prep
%setup -q -n dstat-0.7.2

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dstat

%files data
%defattr(-,root,root,-)
/usr/share/dstat/dstat.py
/usr/share/dstat/dstat.pyc
/usr/share/dstat/dstat.pyo
/usr/share/dstat/dstat_battery.py
/usr/share/dstat/dstat_battery.pyc
/usr/share/dstat/dstat_battery.pyo
/usr/share/dstat/dstat_battery_remain.py
/usr/share/dstat/dstat_battery_remain.pyc
/usr/share/dstat/dstat_battery_remain.pyo
/usr/share/dstat/dstat_cpufreq.py
/usr/share/dstat/dstat_cpufreq.pyc
/usr/share/dstat/dstat_cpufreq.pyo
/usr/share/dstat/dstat_dbus.py
/usr/share/dstat/dstat_dbus.pyc
/usr/share/dstat/dstat_dbus.pyo
/usr/share/dstat/dstat_disk_tps.py
/usr/share/dstat/dstat_disk_tps.pyc
/usr/share/dstat/dstat_disk_tps.pyo
/usr/share/dstat/dstat_disk_util.py
/usr/share/dstat/dstat_disk_util.pyc
/usr/share/dstat/dstat_disk_util.pyo
/usr/share/dstat/dstat_dstat.py
/usr/share/dstat/dstat_dstat.pyc
/usr/share/dstat/dstat_dstat.pyo
/usr/share/dstat/dstat_dstat_cpu.py
/usr/share/dstat/dstat_dstat_cpu.pyc
/usr/share/dstat/dstat_dstat_cpu.pyo
/usr/share/dstat/dstat_dstat_ctxt.py
/usr/share/dstat/dstat_dstat_ctxt.pyc
/usr/share/dstat/dstat_dstat_ctxt.pyo
/usr/share/dstat/dstat_dstat_mem.py
/usr/share/dstat/dstat_dstat_mem.pyc
/usr/share/dstat/dstat_dstat_mem.pyo
/usr/share/dstat/dstat_fan.py
/usr/share/dstat/dstat_fan.pyc
/usr/share/dstat/dstat_fan.pyo
/usr/share/dstat/dstat_freespace.py
/usr/share/dstat/dstat_freespace.pyc
/usr/share/dstat/dstat_freespace.pyo
/usr/share/dstat/dstat_gpfs.py
/usr/share/dstat/dstat_gpfs.pyc
/usr/share/dstat/dstat_gpfs.pyo
/usr/share/dstat/dstat_gpfs_ops.py
/usr/share/dstat/dstat_gpfs_ops.pyc
/usr/share/dstat/dstat_gpfs_ops.pyo
/usr/share/dstat/dstat_helloworld.py
/usr/share/dstat/dstat_helloworld.pyc
/usr/share/dstat/dstat_helloworld.pyo
/usr/share/dstat/dstat_innodb_buffer.py
/usr/share/dstat/dstat_innodb_buffer.pyc
/usr/share/dstat/dstat_innodb_buffer.pyo
/usr/share/dstat/dstat_innodb_io.py
/usr/share/dstat/dstat_innodb_io.pyc
/usr/share/dstat/dstat_innodb_io.pyo
/usr/share/dstat/dstat_innodb_ops.py
/usr/share/dstat/dstat_innodb_ops.pyc
/usr/share/dstat/dstat_innodb_ops.pyo
/usr/share/dstat/dstat_lustre.py
/usr/share/dstat/dstat_lustre.pyc
/usr/share/dstat/dstat_lustre.pyo
/usr/share/dstat/dstat_memcache_hits.py
/usr/share/dstat/dstat_memcache_hits.pyc
/usr/share/dstat/dstat_memcache_hits.pyo
/usr/share/dstat/dstat_mysql5_cmds.py
/usr/share/dstat/dstat_mysql5_cmds.pyc
/usr/share/dstat/dstat_mysql5_cmds.pyo
/usr/share/dstat/dstat_mysql5_conn.py
/usr/share/dstat/dstat_mysql5_conn.pyc
/usr/share/dstat/dstat_mysql5_conn.pyo
/usr/share/dstat/dstat_mysql5_io.py
/usr/share/dstat/dstat_mysql5_io.pyc
/usr/share/dstat/dstat_mysql5_io.pyo
/usr/share/dstat/dstat_mysql5_keys.py
/usr/share/dstat/dstat_mysql5_keys.pyc
/usr/share/dstat/dstat_mysql5_keys.pyo
/usr/share/dstat/dstat_mysql_io.py
/usr/share/dstat/dstat_mysql_io.pyc
/usr/share/dstat/dstat_mysql_io.pyo
/usr/share/dstat/dstat_mysql_keys.py
/usr/share/dstat/dstat_mysql_keys.pyc
/usr/share/dstat/dstat_mysql_keys.pyo
/usr/share/dstat/dstat_net_packets.py
/usr/share/dstat/dstat_net_packets.pyc
/usr/share/dstat/dstat_net_packets.pyo
/usr/share/dstat/dstat_nfs3.py
/usr/share/dstat/dstat_nfs3.pyc
/usr/share/dstat/dstat_nfs3.pyo
/usr/share/dstat/dstat_nfs3_ops.py
/usr/share/dstat/dstat_nfs3_ops.pyc
/usr/share/dstat/dstat_nfs3_ops.pyo
/usr/share/dstat/dstat_nfsd3.py
/usr/share/dstat/dstat_nfsd3.pyc
/usr/share/dstat/dstat_nfsd3.pyo
/usr/share/dstat/dstat_nfsd3_ops.py
/usr/share/dstat/dstat_nfsd3_ops.pyc
/usr/share/dstat/dstat_nfsd3_ops.pyo
/usr/share/dstat/dstat_ntp.py
/usr/share/dstat/dstat_ntp.pyc
/usr/share/dstat/dstat_ntp.pyo
/usr/share/dstat/dstat_postfix.py
/usr/share/dstat/dstat_postfix.pyc
/usr/share/dstat/dstat_postfix.pyo
/usr/share/dstat/dstat_power.py
/usr/share/dstat/dstat_power.pyc
/usr/share/dstat/dstat_power.pyo
/usr/share/dstat/dstat_proc_count.py
/usr/share/dstat/dstat_proc_count.pyc
/usr/share/dstat/dstat_proc_count.pyo
/usr/share/dstat/dstat_qmail.py
/usr/share/dstat/dstat_qmail.pyc
/usr/share/dstat/dstat_qmail.pyo
/usr/share/dstat/dstat_rpc.py
/usr/share/dstat/dstat_rpc.pyc
/usr/share/dstat/dstat_rpc.pyo
/usr/share/dstat/dstat_rpcd.py
/usr/share/dstat/dstat_rpcd.pyc
/usr/share/dstat/dstat_rpcd.pyo
/usr/share/dstat/dstat_sendmail.py
/usr/share/dstat/dstat_sendmail.pyc
/usr/share/dstat/dstat_sendmail.pyo
/usr/share/dstat/dstat_snooze.py
/usr/share/dstat/dstat_snooze.pyc
/usr/share/dstat/dstat_snooze.pyo
/usr/share/dstat/dstat_squid.py
/usr/share/dstat/dstat_squid.pyc
/usr/share/dstat/dstat_squid.pyo
/usr/share/dstat/dstat_test.py
/usr/share/dstat/dstat_test.pyc
/usr/share/dstat/dstat_test.pyo
/usr/share/dstat/dstat_thermal.py
/usr/share/dstat/dstat_thermal.pyc
/usr/share/dstat/dstat_thermal.pyo
/usr/share/dstat/dstat_top_bio.py
/usr/share/dstat/dstat_top_bio.pyc
/usr/share/dstat/dstat_top_bio.pyo
/usr/share/dstat/dstat_top_bio_adv.py
/usr/share/dstat/dstat_top_bio_adv.pyc
/usr/share/dstat/dstat_top_bio_adv.pyo
/usr/share/dstat/dstat_top_childwait.py
/usr/share/dstat/dstat_top_childwait.pyc
/usr/share/dstat/dstat_top_childwait.pyo
/usr/share/dstat/dstat_top_cpu.py
/usr/share/dstat/dstat_top_cpu.pyc
/usr/share/dstat/dstat_top_cpu.pyo
/usr/share/dstat/dstat_top_cpu_adv.py
/usr/share/dstat/dstat_top_cpu_adv.pyc
/usr/share/dstat/dstat_top_cpu_adv.pyo
/usr/share/dstat/dstat_top_cputime.py
/usr/share/dstat/dstat_top_cputime.pyc
/usr/share/dstat/dstat_top_cputime.pyo
/usr/share/dstat/dstat_top_cputime_avg.py
/usr/share/dstat/dstat_top_cputime_avg.pyc
/usr/share/dstat/dstat_top_cputime_avg.pyo
/usr/share/dstat/dstat_top_int.py
/usr/share/dstat/dstat_top_int.pyc
/usr/share/dstat/dstat_top_int.pyo
/usr/share/dstat/dstat_top_io.py
/usr/share/dstat/dstat_top_io.pyc
/usr/share/dstat/dstat_top_io.pyo
/usr/share/dstat/dstat_top_io_adv.py
/usr/share/dstat/dstat_top_io_adv.pyc
/usr/share/dstat/dstat_top_io_adv.pyo
/usr/share/dstat/dstat_top_latency.py
/usr/share/dstat/dstat_top_latency.pyc
/usr/share/dstat/dstat_top_latency.pyo
/usr/share/dstat/dstat_top_latency_avg.py
/usr/share/dstat/dstat_top_latency_avg.pyc
/usr/share/dstat/dstat_top_latency_avg.pyo
/usr/share/dstat/dstat_top_mem.py
/usr/share/dstat/dstat_top_mem.pyc
/usr/share/dstat/dstat_top_mem.pyo
/usr/share/dstat/dstat_top_oom.py
/usr/share/dstat/dstat_top_oom.pyc
/usr/share/dstat/dstat_top_oom.pyo
/usr/share/dstat/dstat_utmp.py
/usr/share/dstat/dstat_utmp.pyc
/usr/share/dstat/dstat_utmp.pyo
/usr/share/dstat/dstat_vm_memctl.py
/usr/share/dstat/dstat_vm_memctl.pyc
/usr/share/dstat/dstat_vm_memctl.pyo
/usr/share/dstat/dstat_vmk_hba.py
/usr/share/dstat/dstat_vmk_hba.pyc
/usr/share/dstat/dstat_vmk_hba.pyo
/usr/share/dstat/dstat_vmk_int.py
/usr/share/dstat/dstat_vmk_int.pyc
/usr/share/dstat/dstat_vmk_int.pyo
/usr/share/dstat/dstat_vmk_nic.py
/usr/share/dstat/dstat_vmk_nic.pyc
/usr/share/dstat/dstat_vmk_nic.pyo
/usr/share/dstat/dstat_vz_cpu.py
/usr/share/dstat/dstat_vz_cpu.pyc
/usr/share/dstat/dstat_vz_cpu.pyo
/usr/share/dstat/dstat_vz_io.py
/usr/share/dstat/dstat_vz_io.pyc
/usr/share/dstat/dstat_vz_io.pyo
/usr/share/dstat/dstat_vz_ubc.py
/usr/share/dstat/dstat_vz_ubc.pyc
/usr/share/dstat/dstat_vz_ubc.pyo
/usr/share/dstat/dstat_wifi.py
/usr/share/dstat/dstat_wifi.pyc
/usr/share/dstat/dstat_wifi.pyo

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
