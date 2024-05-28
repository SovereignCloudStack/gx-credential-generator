import unittest
from datetime import date, datetime

from openstack.image.v2.image import Image as OS_Image

from generator.common import const
from generator.common.gx_schema import (CPU, CheckSum, ChecksumAlgorithm, Disk,
                                        FirmType, HypervisorType, LatestN,
                                        MaintenanceSubscription, Memory,
                                        MemorySize, OperatingSystem, RNGTypes,
                                        Signature, UpdateStrategy, VMDiskType)
from generator.common.gx_schema import VMImage as GX_Image
from generator.common.gx_schema import WatchDogActions
from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.vm_images_discovery import VmImageDiscovery
from tests.common import MockConnection, OpenstackTestcase, get_config

GX_IMAGE_1 = JsonLdObject(
    gx_id="image_1",
    gx_object=GX_Image(
        name="Image1",
        description="Image 1",
        aggregationOfResources=[],
        copyrightOwnedBy=["Fedora-Project"],
        license=["https://docs.fedoraproject.org/en-US/legal/fedora-linux-license/"],
        resourcePolicy=["default: allow intent"],
        checksum=CheckSum(
            checkSumCalculation="sha-512",
            checkSumValue="7f8bababc2c2a94880747383750470aee68c7e8840bb8811eaeda1b0ce71d59f40ebb182",
        ),
        signature=None,
        version=None,
        patchLevel=None,
        buildDate=datetime(2023, 11, 1, 0, 0),
        fileSize=None,
        operatingSystem=OperatingSystem(
            name=None,
            description=None,
            aggregationOfResources=[],
            copyrightOwnedBy=["Fedora-Project"],
            license=[
                "https://docs.fedoraproject.org/en-US/legal/fedora-linux-license/"
            ],
            resourcePolicy=["default: allow intent"],
            checksum=None,
            signature=None,
            version="Stable",
            patchLevel=None,
            buildDate=None,
            osDistribution="Fedora",
        ),
        cpuReq=CPU(
            vendor=None,
            generation=None,
            defaultOversubscriptionRatio=None,
            supportedOversubscriptionRatio=None,
            cpuArchitecture="x86-64",
            cpuFlag=[],
            smtEnabled=False,
            numberOfCores=2,
            numberOfThreads=4,
            baseFrequency=None,
            boostFrequency=None,
            lastLevelCacheSize=None,
            thermalDesignPower=None,
        ),
        gpuReq=None,
        ramReq=Memory(
            vendor=None,
            generation=None,
            defaultOversubscriptionRatio=None,
            supportedOversubscriptionRatio=None,
            memorySize=MemorySize(
                value=1.048576, unit="https://qudt.org/vocab/unit/MegaBYTE"
            ),
            memoryClass="other",
            memoryRank="other",
            eccEnabled=False,
            hardwareEncryption=False,
        ),
        videoRamSize=MemorySize(
            value=20.0, unit="https://qudt.org/vocab/unit/MegaBYTE"
        ),
        rootDiskReq=Disk(
            vendor=None,
            generation=None,
            defaultOversubscriptionRatio=None,
            supportedOversubscriptionRatio=None,
            diskSize=MemorySize(
                value=21.47483648, unit="https://qudt.org/vocab/unit/GigaBYTE"
            ),
            diskType="other",
            diskBusType="SCSI",
        ),
        encryption=None,
        checkSum=None,
        secureBoot=True,
        vPMU=False,
        multiQueues=True,
        updateStrategy=None,
        licenseIncluded=False,
        maintenance={
            "subscriptionIncluded": False,
            "subscriptionRequired": True,
            "maintainedUntil": date(2024, 5, 31),
        },
        vmImageDiskFormat="RAW",
        hypervisorType="other",
        firmwareType="other",
        hwRngTypeOfImage="None",
        watchDogAction="reset",
    ),
)
GX_IMAGE_1.gx_object.maintenance.maintainedUntil = date(2024, 5, 31)

GX_IMAGE_2 = JsonLdObject(
    gx_id="image_2",
    gx_object=GX_Image(
        copyrightOwnedBy=["The FreeBSD Project"],
        license=["GPL-3.0-only", "LGPL-2.0"],
        resourcePolicy=["default: allow intent"],
        maintenance={"subscriptionIncluded": False, "subscriptionRequired": False},
        hypervisorType=HypervisorType("other"),
        operatingSystem=OperatingSystem(
            name=None,
            description=None,
            aggregationOfResources=[],
            copyrightOwnedBy=["The FreeBSD Project"],
            license=["GPL-3.0-only", "LGPL-2.0"],
            resourcePolicy=["default: allow intent"],
            checksum=None,
            signature=None,
            version=None,
            osDistribution="FreeBSD",
        ),
    ),
)

OS_IMAGE_1 = OS_Image(
    hw_scsi_model="virtio - scsi",
    os_distro="Fedora",
    hw_watchdog_action="reset",
    hw_rng_model="virtio",
    os_version="Stable",
    hypervisor_type="qemu",
    hw_video_ram=20,
    hw_vif_multiqueue_enabled=True,
    hw_pmu=False,
    hw_disk_bus="SCSI",
    hw_cpu_cores=2,
    hw_cpu_threads=4,
    architecture="x86_64",
    name="Image2",
    disk_format="RAW",
    container_format="bare",
    needs_secure_boot=True,
    size="9116319744",
    virtual_size="9116319744",
    checksum="a516d5aea8ebc358dd316dd67266a2ba",
    min_ram=1,
    min_disk=20,
    owner="477ba6f14a5b43abe85b2966be7ebe136",
    os_hash_algo="sha512",
    os_hash_value="7f8bababc2c2a94880747383750470aee68c7e8840bb8811eaeda1b0ce71d59f40ebb182",
    id="image_2",
    visibility="public",
    properties={
        "image_build_date": "2023-11-01",
        "image_description": "Image 2",
        "provided_until": "none",
        "replace_frequency": "weekly",
        "uuid_validity": "last-3",
        "patchlevel": "1.5.2",
        "license_required": True,
        "license_included": False,
        "subscription_required": True,
        "subscription_included": False,
        "maintained_until": "2024-05-31",
    },
)
OS_IMAGE_2 = OS_Image(
    os_distro="FreeBSD", id="image_2", visibility="public", lisence_included=False
)


class VMImageDiscoveryTestcase(OpenstackTestcase):
    def setUp(self):
        self.discovery = VmImageDiscovery(
            conn=MockConnection([OS_IMAGE_1, OS_IMAGE_2]), conf=get_config()
        )

    def test_discovery_vm_images(self):
        actual_gax_images = self.discovery.discover()
        self.assert_vm_image(GX_IMAGE_1.gx_object, actual_gax_images[0].gx_object)
        self.assert_vm_image(GX_IMAGE_2.gx_object, actual_gax_images[1].gx_object)

    def test_get_disk_format(self):
        self.assertEqual(
            VMDiskType("RAW"),
            self.discovery._get_disk_format(OS_Image(disk_format="foo")),
        )
        self.assertEqual(
            VMDiskType("RAW"),
            self.discovery._get_disk_format(OS_Image(disk_format="RAW")),
        )
        self.assertEqual(
            VMDiskType("RAW"),
            self.discovery._get_disk_format(OS_Image(disk_format="raw")),
        )
        self.assertEqual(
            VMDiskType("VHD"),
            self.discovery._get_disk_format(OS_Image(disk_format="vHd")),
        )
        self.assertEqual(VMDiskType("RAW"), self.discovery._get_disk_format(OS_Image()))

    def test_get_secure_boot(self):
        self.assertTrue(
            self.discovery._get_secure_boot(OS_Image(needs_secure_boot=True))
        )
        self.assertFalse(
            self.discovery._get_secure_boot(OS_Image(needs_secure_boot=False))
        )
        self.assertFalse(self.discovery._get_secure_boot(OS_Image()))

    def test_get_firmeware_type(self):
        self.assertEqual(
            FirmType(FirmType.BIOS),
            self.discovery._get_firme_ware_type(OS_Image(hw_firmware_type="BIOS")),
        )
        self.assertEqual(
            FirmType(FirmType.BIOS),
            self.discovery._get_firme_ware_type(OS_Image(hw_firmware_type="bioS")),
        )
        self.assertEqual(
            FirmType(FirmType.other),
            self.discovery._get_firme_ware_type(OS_Image(hw_firmware_type="foo")),
        )
        self.assertEqual(
            FirmType(FirmType.other), self.discovery._get_firme_ware_type(OS_Image())
        )

    def test_get_watchdog_action(self):
        self.assertEqual(
            WatchDogActions("reset"),
            self.discovery._get_watchdog_action(OS_Image(hw_watchdog_action="reset")),
        )
        self.assertEqual(
            WatchDogActions("reset"),
            self.discovery._get_watchdog_action(OS_Image(hw_watchdog_action="Reset")),
        )
        self.assertEqual(
            WatchDogActions("disabled"),
            self.discovery._get_watchdog_action(OS_Image(hw_watchdog_action="foo")),
        )
        self.assertEqual(
            WatchDogActions("disabled"), self.discovery._get_watchdog_action(OS_Image())
        )

    def test_get_vmpu(self):
        self.assertTrue(self.discovery._get_vmpu(OS_Image(hw_pmu=True)))
        self.assertFalse(self.discovery._get_vmpu(OS_Image(hw_pmu=False)))
        self.assertFalse(self.discovery._get_vmpu(OS_Image()))

    def test_get_cpu_req(self):
        self.assertEqual(
            CPU(cpuArchitecture="x86-64", numberOfCores=2, numberOfThreads=4),
            self.discovery._get_cpu_req(
                OS_Image(architecture="x86_64", hw_cpu_cores=2, hw_cpu_threads=4)
            ),
        )
        self.assertEqual(
            CPU(cpuArchitecture="x86-64"),
            self.discovery._get_cpu_req(OS_Image(architecture="x86_64")),
        )
        self.assertEqual(
            CPU(cpuArchitecture="other"), self.discovery._get_cpu_req(OS_Image())
        )

    def test_get_multiqueue_enabled(self):
        self.assertTrue(
            self.discovery._get_multiqueue_enabled(
                OS_Image(is_hw_vif_multiqueue_enabled=True)
            )
        )
        self.assertFalse(
            self.discovery._get_multiqueue_enabled(
                OS_Image(is_hw_vif_multiqueue_enabled=False)
            )
        )
        self.assertFalse(self.discovery._get_multiqueue_enabled(OS_Image()))

    def test_get_checksum(self):
        self.assertEqual(
            CheckSum(
                checkSumValue="a123", checkSumCalculation=ChecksumAlgorithm("md5")
            ),
            self.discovery._get_checksum(OS_Image(hash_value="a123", hash_algo="md5")),
        )
        self.assertEqual(
            CheckSum(
                checkSumValue="a123", checkSumCalculation=ChecksumAlgorithm("md5")
            ),
            self.discovery._get_checksum(OS_Image(hash_value="a123", hash_algo="MD5")),
        )
        self.assertEqual(
            CheckSum(
                checkSumValue="a123", checkSumCalculation=ChecksumAlgorithm("other")
            ),
            self.discovery._get_checksum(OS_Image(hash_value="a123", hash_algo="foo")),
        )
        self.assertIsNone(self.discovery._get_checksum(OS_Image()))

    def test_get_rng_model(self):
        self.assertEqual(RNGTypes("None"), self.discovery._get_rng_model(OS_Image()))

    def test_get_file_size(self):
        self.assertEqual(
            MemorySize(value=1.073741824, unit=const.UNIT_GB),
            self.discovery._get_file_size(OS_Image(size=1)),
        )
        self.assertIsNone(self.discovery._get_file_size(OS_Image()))

    def test_get_video_ram(self):
        self.assertEqual(
            MemorySize(value=12, unit=const.UNIT_MB),
            self.discovery._get_video_ram_size(OS_Image(hw_video_ram=12)),
        )
        self.assertIsNone(self.discovery._get_video_ram_size(OS_Image()))

    def test_get_update_strategy(self):
        up_strat = UpdateStrategy(replaceFrequency="monthly", hotfixHours=5)
        # we need to set attributes this way, as constructor converts everything into string
        up_strat.oldVersionsValidUntil = date(2024, 1, 31)
        up_strat.providedUntil = date(2024, 1, 31)

        (
            self.assertEqual(
                up_strat,
                self.discovery._get_update_strategy(
                    OS_Image(
                        replace_frequency="monthly",
                        uuid_validity="2024-01-31",
                        provided_until="2024-01-31",
                        hotfix_hours=5,
                    )
                ),
            ),
        )

        self.assertEqual(
            UpdateStrategy(
                replaceFrequency="yearly",
                oldVersionsValidUntil="forever",
                providedUntil="notice",
                hotfixHours=5,
            ),
            self.discovery._get_update_strategy(
                OS_Image(
                    replace_frequency="yearly",
                    uuid_validity="forever",
                    provided_until="notice",
                    hotfix_hours=5,
                )
            ),
        )

        up_strat = UpdateStrategy(
            replaceFrequency="yearly", providedUntil="notice", hotfixHours=5
        )
        up_strat.oldVersionsValidUntil = LatestN(value=3)
        self.assertEqual(
            up_strat,
            self.discovery._get_update_strategy(
                OS_Image(
                    replace_frequency="yearly",
                    uuid_validity="Latest-3",
                    provided_until="notice",
                    hotfix_hours=5,
                )
            ),
        )
        self.assertEqual(
            UpdateStrategy(),
            self.discovery._get_update_strategy(
                OS_Image(
                    replace_frequency="foo",
                    uuid_validity="foo",
                    provided_until="foo",
                    hotfix_hours=-4,
                )
            ),
        )
        self.assertEqual(
            UpdateStrategy(),
            self.discovery._get_update_strategy(OS_Image(props1="foo")),
        )
        self.assertIsNone(
            self.discovery._get_update_strategy(OS_Image()),
        )

        self.assertIsNone(self.discovery._get_update_strategy(OS_Image()))

    def test_get_description(self):
        self.assertEqual(
            "image",
            self.discovery._get_description(OS_Image(image_description="image")),
        )
        self.assertEqual(
            "image Managed by me",
            self.discovery._get_description(
                OS_Image(image_description="image", managed_by_VENDOR="me")
            ),
        )
        self.assertIsNone(self.discovery._get_description(OS_Image()))

    def test_get_name(self):
        self.assertEqual("image", self.discovery._get_name(OS_Image(name="image")))
        self.assertIsNone(self.discovery._get_name(OS_Image()))

    def test_get_build_date(self):
        self.assertEqual(
            datetime(year=2023, month=12, day=31),
            self.discovery._get_build_date(OS_Image(image_build_date="2023-12-31")),
        )
        self.assertIsNone(self.discovery._get_build_date(OS_Image()))

    def test_get_license_included(self):
        self.assertTrue(
            self.discovery._get_license_included(OS_Image(licenseIncluded=True))
        )
        self.assertFalse(
            self.discovery._get_license_included(OS_Image(licenseIncluded=False))
        )
        self.assertFalse(self.discovery._get_license_included(OS_Image()))

    def test_get_patch_level(self):
        self.assertEqual(
            "v1.2.0", self.discovery._get_patch_level(OS_Image(patchlevel="v1.2.0"))
        )
        self.assertIsNone(self.discovery._get_patch_level(OS_Image(propo1="foo")))
        self.assertIsNone(self.discovery._get_patch_level(OS_Image()))

    def test_get_version(self):
        self.assertEqual(
            "v1.2.0", self.discovery._get_version(OS_Image(internal_version="v1.2.0"))
        )
        self.assertIsNone(self.discovery._get_version(OS_Image()))

    def test_get_maintenance(self):
        maint = MaintenanceSubscription(
            subscriptionIncluded=True,
            subscriptionRequired=True,
        )
        # we need to set this property explicitly, as constructor converts date to string
        maint.maintainedUntil = date(2024, 5, 31)
        self.assertEqual(
            maint,
            self.discovery._get_maintenance(
                OS_Image(
                    subscription_required=True,
                    subscription_included=True,
                    maintained_until="2024-05-31",
                )
            ),
        )
        self.assertEqual(
            MaintenanceSubscription(
                subscriptionIncluded=True, subscriptionRequired=True
            ),
            self.discovery._get_maintenance(
                OS_Image(subscription_required=True, subscription_included=True)
            ),
        )
        self.assertEqual(
            MaintenanceSubscription(
                subscriptionIncluded=False, subscriptionRequired=True
            ),
            self.discovery._get_maintenance(OS_Image(subscription_required=True)),
        )
        self.assertEqual(
            MaintenanceSubscription(
                subscriptionIncluded=False, subscriptionRequired=False
            ),
            self.discovery._get_maintenance(OS_Image()),
        )

    def test_get_signature(self):
        self.assertEqual(
            Signature(
                signatureValue="e123",
                hashAlgorithm=ChecksumAlgorithm.md5,
                signatureAlgorithm="RSA-Signature",
            ),
            self.discovery._get_signature(
                OS_Image(
                    img_signature="e123",
                    img_signature_hash_method="md5",
                    img_signature_key_type="SHA-123",
                )
            ),
        )
        self.assertEqual(
            Signature(
                signatureValue="e123",
                hashAlgorithm=ChecksumAlgorithm.md5,
                signatureAlgorithm="RSA-Signature",
            ),
            self.discovery._get_signature(
                OS_Image(
                    img_signature="e123",
                    img_signature_hash_method="MD5",
                    img_signature_key_type="Sha-123",
                )
            ),
        )
        self.assertEqual(
            Signature(
                signatureValue="e123",
                hashAlgorithm=ChecksumAlgorithm.other,
                signatureAlgorithm="other",
            ),
            self.discovery._get_signature(
                OS_Image(
                    img_signature="e123",
                    img_signature_hash_method="bar",
                    img_signature_key_type="foo",
                )
            ),
        )
        self.assertIsNone(self.discovery._get_signature(OS_Image()))

    def test_get_hypervisor(self):
        self.assertEqual(
            HypervisorType("KVM"),
            self.discovery._get_hypervisor_type(OS_Image(hypervisor_type="KVM")),
        )
        self.assertEqual(
            HypervisorType("KVM"),
            self.discovery._get_hypervisor_type(OS_Image(hypervisor_type="Kvm")),
        )
        self.assertIsNone(self.discovery._get_min_ram_req(OS_Image(props="foo")))
        self.assertIsNone(self.discovery._get_min_ram_req(OS_Image()))

    def test_get_min_ram_req(self):
        self.assertEqual(
            Memory(
                memorySize=MemorySize(1.048576, unit=const.UNIT_MB),
                hardwareEncryption=True,
            ),
            self.discovery._get_min_ram_req(
                OS_Image(min_ram=1, hw_mem_encryption=True)
            ),
        )
        self.assertEqual(
            Memory(
                memorySize=MemorySize(0, unit=const.UNIT_MB), hardwareEncryption=False
            ),
            self.discovery._get_min_ram_req(OS_Image(min_ram=0)),
        )
        self.assertIsNone(self.discovery._get_min_ram_req(OS_Image()))

    def test_get_min_disk_req(self):
        self.assertEqual(
            Disk(
                diskSize=MemorySize(1.073741824, unit=const.UNIT_GB), diskBusType="SATA"
            ),
            self.discovery._get_min_disk_req(OS_Image(min_disk=1, hw_disk_bus="SATA")),
        )
        self.assertEqual(
            Disk(diskSize=MemorySize(0, unit=const.UNIT_GB), diskBusType="other"),
            self.discovery._get_min_disk_req(OS_Image(min_disk=0)),
        )
        self.assertIsNone(self.discovery._get_min_disk_req(OS_Image()))

    def test_get_operating_system(self):
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_ALP,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Alpine Linux",
                license=["https://gitlab.alpinelinux.org/alpine/aports/-/issues/9074"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="alpinelinux")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_ALMA_LINUX,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Canonical Ltd.",
                license=["https://almalinux.org/p/the-almalinux-os-licensing-policy/"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="AlmaLinux")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_ARCH,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Judd Vinet, Aaron Griffin, Levente Polyák and others",
                license=["https://gitlab.archlinux.org/archlinux"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="arch")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_CENTOS,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="The CentOS Project and others",
                license=["https://github.com/CentOS/"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="centOs")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_CIRROS,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Canonical Ltd.",
                license=["GPL-2.0-only"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="cirros")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_DEBIAN,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Ian Murdock and others",
                license=["https://www.debian.org/legal/licenses/index.en.html"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="debian")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_FREEBSD,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="The FreeBSD Project",
                license=["GPL-3.0-only", "LGPL-2.0"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="FreeBSD")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_FEDORA,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Fedora-Project",
                license=[
                    "https://docs.fedoraproject.org/en-US/legal/fedora-linux-license/"
                ],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="fedora")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_GENTOO,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Gentoo Foundation, Inc.",
                license=["https://www.gentoo.org/glep/glep-0076.html"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="gentoo")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_MANDRAKE,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Mandriva Linux",
                license=["GPL-3.0-only"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="mandrake")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_MANDRIVA,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Mandriva S. A.",
                license=["GPL-3.0-only"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="mandriva")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_MES,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Mandriva S. A.",
                license=["GPL-3.0-only"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="mes")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_MSDOS,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Microsoft Corporation",
                license=[
                    "https://www.microsoft.com/licensing/docs/view/Licensing-Guides"
                ],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="msdos")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_NETBSD,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="The NetBSD Foundation",
                license=["https://www.netbsd.org/about/redistribution.html"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="netbsd")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_NOVELL,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Micro Focus International",
                license=[
                    "https://support.novell.com/techcenter/articles/ana19960702.html"
                ],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="netware")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_OPENBSD,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="OpenBSD",
                license=["https://www.openbsd.org/policy.html"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="openbsd")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_OPEN_SUSE,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="openSUSE contributors & others",
                license=["https://en.opensuse.org/openSUSE:License"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="opensuse")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_SOLARIS,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Sun Microsystems",
                license=[
                    "https://opensource.apple.com/source/xnu/xnu-2050.7.9/tools/tests/libMicro/OPENSOLARIS.LICENSE.auto.html"
                ],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="opensolaris")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_ROCKY,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Rocky Enterprise Software Foundation",
                license=["https://rockylinux.org/licensing"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="rocky")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_RHEL,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Red Hat, Inc.",
                license=[
                    "https://www.redhat.com/en/store/red-hat-enterprise-linux-server"
                ],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="rhel")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_SUSE,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="openSUSE contributors & others",
                license=["https://www.suse.com/products/terms_and_conditions.pdf"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="suse")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution="others",
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="TBA",
                license=["TBA"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="sled")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_UBUNTU,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Canonical",
                license=["https://ubuntu.com/legal/open-source-licences"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="ubuntu")
            ),
        )
        self.assertEqual(
            OperatingSystem(
                version="1",
                osDistribution=const.CONFIG_OS_WINDOWS,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="Microsoft Corporation",
                license=["https://www.microsoft.com/licensing"],
            ),
            self.discovery._get_operation_system(
                OS_Image(os_version="1", os_distro="windows")
            ),
        )


if __name__ == "__main__":
    unittest.main()
