#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dstat
Version  : 0.7.3
Release  : 20
URL      : https://github.com/dagwieers/dstat/archive/0.7.3.tar.gz
Source0  : https://github.com/dagwieers/dstat/archive/0.7.3.tar.gz
Summary  : Pluggable real-time performance monitoring tool
Group    : Development/Tools
License  : GPL-2.0
Requires: dstat-bin = %{version}-%{release}
Requires: dstat-data = %{version}-%{release}
Requires: dstat-license = %{version}-%{release}
Requires: dstat-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : docbook-xml
BuildRequires : libxslt-bin
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : util-linux
BuildRequires : xmlto
Patch1: 0001-Bring-0.7.3-tag-to-master-HEAD.patch
Patch2: 0002-porting-to-python-3-just-work-only.patch
Patch3: 0003-Fix-whitespace.patch
Patch4: 0004-Skip-XML-document-validation.patch

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
Requires: dstat-data = %{version}-%{release}
Requires: dstat-license = %{version}-%{release}
Requires: dstat-man = %{version}-%{release}

%description bin
bin components for the dstat package.


%package data
Summary: data components for the dstat package.
Group: Data

%description data
data components for the dstat package.


%package license
Summary: license components for the dstat package.
Group: Default

%description license
license components for the dstat package.


%package man
Summary: man components for the dstat package.
Group: Default

%description man
man components for the dstat package.


%prep
%setup -q -n dstat-0.7.3
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542484103
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1542484103
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dstat
cp COPYING %{buildroot}/usr/share/package-licenses/dstat/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dstat

%files data
%defattr(-,root,root,-)
/usr/share/dstat/dstat.py
/usr/share/dstat/dstat_battery.py
/usr/share/dstat/dstat_battery_remain.py
/usr/share/dstat/dstat_condor_queue.py
/usr/share/dstat/dstat_cpufreq.py
/usr/share/dstat/dstat_dbus.py
/usr/share/dstat/dstat_disk_avgqu.py
/usr/share/dstat/dstat_disk_avgrq.py
/usr/share/dstat/dstat_disk_svctm.py
/usr/share/dstat/dstat_disk_tps.py
/usr/share/dstat/dstat_disk_util.py
/usr/share/dstat/dstat_disk_wait.py
/usr/share/dstat/dstat_dstat.py
/usr/share/dstat/dstat_dstat_cpu.py
/usr/share/dstat/dstat_dstat_ctxt.py
/usr/share/dstat/dstat_dstat_mem.py
/usr/share/dstat/dstat_fan.py
/usr/share/dstat/dstat_freespace.py
/usr/share/dstat/dstat_fuse.py
/usr/share/dstat/dstat_gpfs.py
/usr/share/dstat/dstat_gpfs_ops.py
/usr/share/dstat/dstat_helloworld.py
/usr/share/dstat/dstat_ib.py
/usr/share/dstat/dstat_innodb_buffer.py
/usr/share/dstat/dstat_innodb_io.py
/usr/share/dstat/dstat_innodb_ops.py
/usr/share/dstat/dstat_jvm_full.py
/usr/share/dstat/dstat_jvm_vm.py
/usr/share/dstat/dstat_lustre.py
/usr/share/dstat/dstat_md_status.py
/usr/share/dstat/dstat_memcache_hits.py
/usr/share/dstat/dstat_mongodb_conn.py
/usr/share/dstat/dstat_mongodb_mem.py
/usr/share/dstat/dstat_mongodb_opcount.py
/usr/share/dstat/dstat_mongodb_queue.py
/usr/share/dstat/dstat_mongodb_stats.py
/usr/share/dstat/dstat_mysql5_cmds.py
/usr/share/dstat/dstat_mysql5_conn.py
/usr/share/dstat/dstat_mysql5_innodb.py
/usr/share/dstat/dstat_mysql5_innodb_basic.py
/usr/share/dstat/dstat_mysql5_innodb_extra.py
/usr/share/dstat/dstat_mysql5_io.py
/usr/share/dstat/dstat_mysql5_keys.py
/usr/share/dstat/dstat_mysql_io.py
/usr/share/dstat/dstat_mysql_keys.py
/usr/share/dstat/dstat_net_packets.py
/usr/share/dstat/dstat_nfs3.py
/usr/share/dstat/dstat_nfs3_ops.py
/usr/share/dstat/dstat_nfsd3.py
/usr/share/dstat/dstat_nfsd3_ops.py
/usr/share/dstat/dstat_nfsd4_ops.py
/usr/share/dstat/dstat_nfsstat4.py
/usr/share/dstat/dstat_ntp.py
/usr/share/dstat/dstat_postfix.py
/usr/share/dstat/dstat_power.py
/usr/share/dstat/dstat_proc_count.py
/usr/share/dstat/dstat_qmail.py
/usr/share/dstat/dstat_redis.py
/usr/share/dstat/dstat_rpc.py
/usr/share/dstat/dstat_rpcd.py
/usr/share/dstat/dstat_sendmail.py
/usr/share/dstat/dstat_snmp_cpu.py
/usr/share/dstat/dstat_snmp_load.py
/usr/share/dstat/dstat_snmp_mem.py
/usr/share/dstat/dstat_snmp_net.py
/usr/share/dstat/dstat_snmp_net_err.py
/usr/share/dstat/dstat_snmp_sys.py
/usr/share/dstat/dstat_snooze.py
/usr/share/dstat/dstat_squid.py
/usr/share/dstat/dstat_test.py
/usr/share/dstat/dstat_thermal.py
/usr/share/dstat/dstat_top_bio.py
/usr/share/dstat/dstat_top_bio_adv.py
/usr/share/dstat/dstat_top_childwait.py
/usr/share/dstat/dstat_top_cpu.py
/usr/share/dstat/dstat_top_cpu_adv.py
/usr/share/dstat/dstat_top_cputime.py
/usr/share/dstat/dstat_top_cputime_avg.py
/usr/share/dstat/dstat_top_int.py
/usr/share/dstat/dstat_top_io.py
/usr/share/dstat/dstat_top_io_adv.py
/usr/share/dstat/dstat_top_latency.py
/usr/share/dstat/dstat_top_latency_avg.py
/usr/share/dstat/dstat_top_mem.py
/usr/share/dstat/dstat_top_oom.py
/usr/share/dstat/dstat_utmp.py
/usr/share/dstat/dstat_vm_cpu.py
/usr/share/dstat/dstat_vm_mem.py
/usr/share/dstat/dstat_vm_mem_adv.py
/usr/share/dstat/dstat_vmk_hba.py
/usr/share/dstat/dstat_vmk_int.py
/usr/share/dstat/dstat_vmk_nic.py
/usr/share/dstat/dstat_vz_cpu.py
/usr/share/dstat/dstat_vz_io.py
/usr/share/dstat/dstat_vz_ubc.py
/usr/share/dstat/dstat_wifi.py
/usr/share/dstat/dstat_zfs_arc.py
/usr/share/dstat/dstat_zfs_l2arc.py
/usr/share/dstat/dstat_zfs_zil.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dstat/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dstat.1
