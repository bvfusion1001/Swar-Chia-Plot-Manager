def format_config_info(config_jobs):
    job_1 = config_jobs[0]
    max_plots = str(job_1.get('max_plots'))
    threads = str(job_1.get('threads'))
    memory_buffer = str(job_1.get('memory_buffer'))
    stagger_minutes = str(job_1.get('stagger_minutes'))
    max_concurrent = str(job_1.get('max_concurrent'))
    max_concurrent_with_start_early = str(job_1.get('max_concurrent_with_start_early'))
    max_for_phase_1 = str(job_1.get('max_for_phase_1'))
    concurrency_start_early_phase = str(job_1.get('concurrency_start_early_phase'))
    concurrency_start_early_phase_delay = str(job_1.get('concurrency_start_early_phase_delay'))
    temporary2_destination_sync = str(job_1.get('temporary2_destination_sync'))

    headers1 = ['Plots', 'Threads' ,'RAM' , 'Stagger', 'P1 Max']
    values1 = [max_plots, threads, memory_buffer, stagger_minutes, max_for_phase_1]
    pretty_config_table1 = pretty_print_table([headers1] + [values1])

    headers2 = ['MaxConc', 'MC SEarly', 'CSEPhase', 'CSEPDelay']
    values2 = [max_concurrent, max_concurrent_with_start_early, concurrency_start_early_phase, concurrency_start_early_phase_delay]
    pretty_config_table2 = pretty_print_table([headers2] + [values2])
    return f'{pretty_config_table1}\n{pretty_config_table2}'

def pretty_print_table(rows):
    max_characters = [0 for cell in rows[0]]
    for row in rows:
        for i, cell in enumerate(row):
            length = len(cell)
            if len(cell) <= max_characters[i]:
                continue
            max_characters[i] = length

    headers = "   ".join([cell.center(max_characters[i]) for i, cell in enumerate(rows[0])])
    separator = '=' * ((sum(max_characters) + 3 * len(max_characters)) - 13)
    console = [separator, headers, separator]
    for row in rows[1:]:
        console.append("   ".join([cell.ljust(max_characters[i]) for i, cell in enumerate(row)]))
    # console.append(separator)
    return "\n".join(console)